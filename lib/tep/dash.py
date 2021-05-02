import os
import shutil
from pathlib import Path

class DashboardObject:
    def __init__(self, title, description = ""):
        self.title = title
        self.description = description
        self.dependencies = []
    
    def build(self, path, f):
        for dep in self.dependencies:
            shutil.copyfile(dep, path.joinpath(dep.name))
        self.render(f)

    def render(self, f):
        f.write(f"<h2>{self.title}</h2>")
        f.write(f"<p>{self.description}</p>")
        self._render(f)

    def _render(self, f):
        pass


class Image(DashboardObject):
    def __init__(self, path, title, description = ""):
        super().__init__(title, description)
        self.path = Path(path)
        self.dependencies.append(self.path)
    
    def _render(self, f):
        f.write(f"<img src='{self.path.name}'>")


class Dashboard:
    def __init__(self, out_dir="dashboard"):
        self.out_dir = Path(out_dir)
        self._built = False
        self._objects = []

    def add(self, obj):
        self._objects.append(obj)
        return self

    def build(self):
        self.out_dir.mkdir(exist_ok = True)

        with open(self.out_dir.joinpath("index.html"), "w") as f:
            f.write("""<!DOCTYPE html>
                <html>
                    <head>
                        <title>WARA-SW TEP Dashboard</title>
                        <meta charset="utf-8"/>
                    </head>
                    <body>
                        <center>
                    """)

            for obj in self._objects:
                obj.build(self.out_dir, f)

            f.write("""</center>
                </body>
                </html>
                """)
            self._built = True

    def serve(self):
        assert(self._built)
