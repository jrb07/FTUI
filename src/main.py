import importlib
import importlib.util
import subprocess
import sys

def install(packages):
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"{package!r} is already installed")
        except ImportError as error:
            print(error)
            print(f"INSTALLING {package!r}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print("Package installed")
            except:
                print("INVALID PACKAGE CANNOT INSTALL")

packages_to_install = ["numpy", "opencv-python", "textual"]

install(packages_to_install)

import numpy as np
import cv2
from textual import containers, lazy
from textual.app import App, ComposeResult
from textual.demo.page import PageScreen
from textual.widgets import Markdown

class MyScreen(PageScreen):
    MAIN_MD = """ \n
# Welcome to the Figure Terminal User Interface (FTUI)

[FTUI Github repo](https://github.com/jrb07/FTUI)

Press ctrl+q to exit

Author: Jeremy Ryan Brown \n
All rights reserved.
"""
    def compose(self) -> ComposeResult:
        with lazy.Reveal(containers.VerticalScroll(can_focus=True)):
            yield Markdown(self.MAIN_MD)

if __name__ == "__main__":
    class AppManager(App):
        def get_default_screen(self) -> MyScreen:
            return MyScreen()
    app = AppManager()
    app.run()

