import json

import yaml


def convert_file_data_to_dict(
    file_1_data: str, file_2_data: str, files_format: str
) -> tuple[dict, dict]:
    """
    Returns a tuple of dicts containing data from provided files

    :param file_1_data: data from the first file
    :param file_2_data: data from the second file
    :param files_format: the format of files
    :return: tuple that contains two dict elements
    """

    if files_format == "yml":
        return yaml.load(file_1_data, yaml.SafeLoader), yaml.load(
            file_2_data, yaml.SafeLoader
        )
    if files_format == "json":
        return json.loads(file_1_data), json.loads(file_2_data)
