from tep.dashboard import Dashboard

import yaml
import os
import sys
import shutil
from pathlib import Path

import plotly.express as px
import dash
from dash import html
from dash import dcc

import tep_dashboard as tdc


class DashboardApp:
    def __init__(self):
        self.asset_dir = Path(os.environ["OVE_OWEL_DIR"]).joinpath("dashboard/assets")
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

    def dashboard_info(self):
        return dict([(key, dash.title) for (key, dash) in self._dashboards.items()])

    def serve(self):
        assert(self._built)

        self._app.layout = html.Div(children=[
            dcc.Location(id="url", refresh=False),
            html.Div([], id="dashboard-area"),
        ])
        self._app.run_server(debug=True, host="0.0.0.0")

    def asset(self, path):
        return self._app.get_asset_url(str(Path("figures").joinpath(path)))

app = DashboardApp()

def load_dashboard(name, path=None):
    if path == None:
        path = name
    try:
        G = {}
        exec(Path(os.environ["OVE_OWEL_DIR"]).joinpath(f"projects/{name}/dash").open().read(), G)
        app.add(path, G["dashboard"])
    except FileNotFoundError:
        print(f"failed to load dashboard {name}")

@app._app.callback(
    dash.dependencies.Output("dashboard-area", "children"),
    dash.dependencies.Input("url", "pathname")
    )
def show_dashboard(path):
    key = path[1:]

    if key == "":
        key = "home"

    print("Showing dashboard: " + key)

    dash = app.get_dashboard(key)
    print(app.dashboard_info())

    if dash:
        return tdc.Dashboard(
            id="dashboard",
            selected=key,
            dashboards=app.dashboard_info(),
            children=dash.render()
        ),
    else:
        return tdc.Dashboard(
            id="dashboard",
            selected="",
            dashboards=app.dashboard_info(),
            children=[]
        )

with open(Path(os.environ["OVE_OWEL_DIR"]).joinpath("projs")) as f:
    projects = yaml.safe_load(f)

load_dashboard("dashboard_components", "home")
for project in sys.argv:
    if project in projects:
        load_dashboard(project)

app.build()
app.serve()
