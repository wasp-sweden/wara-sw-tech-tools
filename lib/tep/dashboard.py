import os
import shutil
from pathlib import Path

import dash
from dash import html
from dash import dcc

class DashboardObject:
    def __init__(self, title, description = "", dependencies = [], meta = None):
        self.title = title
        self.description = description
        self.dependencies = dependencies
        self.meta = meta
    
    def build(self, path):
        for dep in self.dependencies:
            shutil.copyfile(dep, path.joinpath(dep.name))

    def render(self, dashboard):
        return html.Div(children=[
            html.H2(self.title),
            html.H3(self.meta["timestamp"]),
            dcc.Markdown(self.description),
            html.Pre(self.meta["env"]["uname"]),
            self._render(dashboard)
        ], className="dashboard-object")

    def _render(self, dashboard):
        pass


class Graph(DashboardObject):
    def __init__(self, figure, title, description = "", meta = None):
        super().__init__(title, description, meta=meta)
        figure.update_layout(template="plotly_dark")
        self._figure = figure

    def _render(self, dashboard):
        return dcc.Graph(figure=self._figure)


class Component(DashboardObject):
    def __init__(self, component, title, description = "", dependencies = []):
        super().__init__(title, description, dependencies)
        self._component = component

    def _render(self, dashboard):
        return self._component


class Image(DashboardObject):
    def __init__(self, path, title, description = ""):
        super().__init__(title, description)
        self.path = Path(path)
        self.dependencies.append(self.path)
    
    def _render(self, dashboard):
        return html.Img(src=dashboard.asset(self.path.name))


class Dashboard:
    def __init__(self, title):
        self.title = title
        self.asset_dir = Path(os.environ["OVE_PROJECT_DIR"]).joinpath("dashboard/assets")
        self.figure_dir = self.asset_dir.joinpath("figures")
        self._built = False
        self._objects = []
        self._app = dash.Dash(__name__, assets_folder=self.asset_dir.absolute())

    def add(self, obj):
        self._objects.append(obj)
        return self

    def build(self):
        self.figure_dir.mkdir(parents = True, exist_ok = True)
        for obj in self._objects:
            obj.build(self.figure_dir)

        self._built = True
        return self

    def render(self):
        return html.Main([obj.render(self) for obj in self._objects])
    

    def serve(self):
        assert(self._built)

        self._app.layout = html.Div(children=[
            html.H1(["WARA-SW TEP Dashboard: ", html.B(self.title)]),
            self.render()
        ])
        self._app.run_server(debug=True)

    def asset(self, path):
        return self._app.get_asset_url(str(Path("figures").joinpath(path)))
