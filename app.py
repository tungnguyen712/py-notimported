"""Sample app for the ground-truth tests. It pins vulnerable dependency
versions ON PURPOSE. Never install or deploy it.

The vulnerable packages are in the manifest (left over from earlier work) but
nothing imports them.
"""
import json
import os

import requests


def fetch(url):
    response = requests.get(url, timeout=10)
    return json.loads(response.text), os.environ.get("HOME")
