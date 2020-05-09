import json
from json.decoder import JSONDecodeError


class Brain:
    def __init__(self, brain_file_path):
        self.file_path = brain_file_path

        self.load_file()

    def load_file(self):
        try:
            with open(self.file_path, "r") as f:
                self.brain_json = json.load(f)
        except JSONDecodeError:
            # TODO: Logging
            print("No last analyzed tweet to load")
        except FileNotFoundError:
            # Who cares we'll make/write the file at the end
            pass

    def save_file(self):
        with open(self.file_path, "w+") as f:
            json.dump(self.brain_json, f, indent=4)

    def list_tags(self):
        return self.brain_json.keys()

    def keys(self):
        return self.list_tags()

    def __getitem__(self, attr):
        return self.brain_json.get(attr, {})

    def __setitem__(self, attr, value):
        self.brain_json[attr] = value

    def __repr__(self):
        return f"{self.brain_json}"
