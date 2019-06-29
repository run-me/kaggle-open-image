import json
from tqdm import tqdm

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
    json_file_path = "/media/mash-compute/mWm_drive_00/dataset/kaggle_open_image/test.json"

    def create(self, dict, save_path):
        with open(save_path, 'r+') as jf:
            json_dict = json.load(jf)

        with open(save_path, 'w+') as wjf:
            # print(json_data)
            json.dump(dict, jf)

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def save_dict_to_json(self, save_dict):
        with open(JsonCRUD.json_file_path, 'w+') as f:
            json.dump(save_dict, f)


# test functions here
if __name__ == "__main__":
    # test_dict = {"1": "test1", "2": "test2"}
    # JsonCRUD().save_dict_to_json({"parent_1": test_dict, "parent_2": test_dict})

    # tqdm test
    my_list = list(range(100000000))
    for x in tqdm(my_list):
        a = 1
        b = 2
        c = a * b
