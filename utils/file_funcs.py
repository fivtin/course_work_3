import os
import json


def load_from_file():
    """load operations from json file"""
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_dir, "..", "data", "operations.json"), encoding="UTF-8") as f:
        return json.loads(f.read())
