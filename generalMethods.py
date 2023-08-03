import json
# static method(s) that are necessary for the plugin


def write_to_json_file(data, filename, mode):
    with open(filename, mode) as f:
        json.dump(data, f, indent=2)
