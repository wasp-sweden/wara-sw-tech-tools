from tep.dashboard import Dashboard

import yaml
import os
import sys
import shutil
from pathlib import Path

import dash
from dash import html
from dash import dcc


class DashboardApp:
    def __init__(self):
        self.asset_dir = Path(os.environ["OVE_PROJECT_DIR"]).joinpath("dashboard/assets")
        self.figure_dir = self.asset_dir.joinpath("figures")
        self._built = False
        self._dashboards = {}
        self._app = dash.Dash(__name__, assets_folder=self.asset_dir.absolute())

    def add(self, name, dashboard):
        self._dashboards[name] = dashboard
        return self

    def build(self):
        self.figure_dir.mkdir(parents = True, exist_ok = True)
        for (name, dash) in self._dashboards.items():
            dash.build()

        self._built = True
        return self

    def get_dashboard(self, name):
        if name in self._dashboards:
            return self._dashboards[name]
        else:
            return None

    def serve(self):
        assert(self._built)

        self._app.layout = html.Div(children=[
            dcc.Location(id="url", refresh=False),
            html.H1(["WARA-SW TEP Dashboard"]),
            html.Main([
                html.Div([
                    html.A(dashboard.title, href="/" + name),
                ])
                for (name, dashboard) in self._dashboards.items()
            ]),
            html.Div([], id="dashboard-area")
        ])
        self._app.run_server(debug=True, host="0.0.0.0")

    def asset(self, path):
        return self._app.get_asset_url(str(Path("figures").joinpath(path)))

app = DashboardApp()

def load_dashboard(name):
    try:
        G = {}
        exec(Path(os.environ["OVE_PROJECT_DIR"]).joinpath(f"projects/{name}/dash").open().read(), G)
        app.add(name, G["dashboard"])
    except FileNotFoundError:
        print(f"failed to load dashboard {name}")

#load_dashboard("vaccinate")
#load_dashboard("depclean")

@app._app.callback(
    dash.dependencies.Output("dashboard-area", "children"),
    dash.dependencies.Input("url", "pathname")
    )
def show_dashboard(name):
    print(name)
    dash = app.get_dashboard(name[1:])
    if dash:
        return dash.render()
    else:
        return []

with open(Path(os.environ["OVE_PROJECT_DIR"]).joinpath("projs")) as f:
    projects = yaml.safe_load(f)

for project in sys.argv:
    if project in projects:
        load_dashboard(project)

app.build()
app.serve()
