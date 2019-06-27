import json

json_string = """
{
"test": {
    "name": "Ford Prefect",
    "species": "Betelgeusian",
    "relatives": [
            {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
            }
            ]
    }
}
"""

class JsonCRUD:
    def __init__(self, json_path):
        self.json_file_path = json_path

    def save_json(self, dict, save_path):
        with open(save_path, 'r+') as jf:
            json_dict = json.load(jf)

        with open(save_path, 'w+') as wjf:
            print(json_data)
            json.dump(dict, jf)