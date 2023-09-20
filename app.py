#!/usr/bin/env ipython3

"""
A flask app that, when you hit a path, returns the file contents as a string.
"""

from flask import Flask
from pathlib import Path

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "7d441f27d441f27567d441f2b6176a"

MOUNT_POINT="/host" # where host FS is mounted
ENDPOINT = "/get"

@app.route('/get/<path:file_path>')
def get_file(file_path):
    path = Path(MOUNT_POINT) / Path(file_path)
    content = path.read_text()
    return content # TODO

if __name__ == "__main__":
    app.run()
