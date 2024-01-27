import os
import json


def load_from_file():
    """"""
    with open(os.path.join("..", "data", "operations.json"), encoding="UTF-8") as f:
        return json.loads(f.read())
    # try:
    #     with open(os.path.join("..", "data", "operations.json"), encoding="UTF-8") as f:
    #         return json.loads(f.read())
    # except FileNotFoundError:
    #     return []
