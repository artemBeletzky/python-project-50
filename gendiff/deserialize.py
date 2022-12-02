import json
import yaml
from .read_data import read_files_from_disk


def convert_files_to_dict(
    path_to_file_1: str, path_to_file_2: str
) -> tuple[dict, dict]:
    """
    Returns a tuple of dicts containing data from provided files

    :param path_to_file_1: path to the first file
    :param path_to_file_2: path to the second file
    :return: tuple that contains two dict elements
    """
    file_1_data, file_2_data = read_files_from_disk(
        path_to_file_1, path_to_file_2
    )
    if (
        path_to_file_1.split(".")[1] == "yml"
        and path_to_file_2.split(".")[1] == "yml"
    ):
        file_1_converted, file_2_converted = yaml.load(
            file_1_data, yaml.SafeLoader
        ), yaml.load(file_2_data, yaml.SafeLoader)
    elif (
        path_to_file_1.split(".")[1] == "json"
        and path_to_file_2.split(".")[1] == "json"
    ):
        file_1_converted, file_2_converted = json.loads(
            file_1_data
        ), json.loads(file_2_data)
    else:
        raise Exception(
            """File extension is not supported or files has extensions
            that aren't the same, both files should have .json or .yml
            extensions."""
        )
    return file_1_converted, file_2_converted
