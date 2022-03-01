import os
import shutil
from pathlib import Path

import dash
from dash import html
from dash import dcc

from tep_dashboard import Dashboard

class Dashboard:
    def __init__(self, title):
        self.title = title
        self._widgets = []

    def add(self, widget):
        self._widgets.append(widget)
        return self

    def build(self):
        self._built = True
        return self

    def render(self):
        return self._widgets

