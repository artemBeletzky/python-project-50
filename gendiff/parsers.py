import json
import yaml
import os


def parse_file_to_dict(path_to_file_1: str, path_to_file_2: str) -> tuple:
    file_1_path, file_2_path = os.path.abspath(path_to_file_1), os.path.abspath(
        path_to_file_2
    )
    with open(file_1_path, "r") as file_1, open(file_2_path, "r") as file_2:
        if (
            file_1_path.split(".")[1] == "yml"
            and file_2_path.split(".")[1] == "yml"
        ):
            file_1_dict, file_2_dict = yaml.load(
                file_1, yaml.SafeLoader
            ), yaml.load(file_2, yaml.SafeLoader)
        elif (
            file_1_path.split(".")[1] == "json"
            and file_2_path.split(".")[1] == "json"
        ):
            file_1_dict, file_2_dict = json.load(file_1), json.load(file_2)
        else:
            raise IOError(
                "File extension is not supported or files extensions aren't "
                "the same, both files should have .json or .yml extensions."
            )
            # TODO exception?
    return file_1_dict, file_2_dict


print(
    parse_file_to_dict("tests/fixtures/file1.json", "tests/fixtures/file2.json")
)
