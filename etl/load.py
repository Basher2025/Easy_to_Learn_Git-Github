import json
# let's create a JSON file here


def load_data_to_json(rows, path="data/output.json"):
    with open(path, "w") as f:
        json.dump(rows, f, indent=2)
