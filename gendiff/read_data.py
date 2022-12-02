import pathlib


def read_files_from_disk(
    path_to_file_1: str, path_to_file_2: str
) -> tuple[str, str]:
    """
    Returns data read from disk

    :param path_to_file_1: path to the first file
    :param path_to_file_2: path to the second file
    :return: tuple that contains text data read from files
    """
    joined_paths = tuple(
        map(
            lambda path: (pathlib.Path().cwd().joinpath(path)),
            (path_to_file_1, path_to_file_2),
        )
    )
    file_1_path_joined, file_2_path_joined = joined_paths
    with open(file_1_path_joined, "r") as f_1, open(
        file_2_path_joined, "r"
    ) as f_2:
        file_1_data, file_2_data = f_1.read(), f_2.read()
    print(file_1_data, file_2_data)
    return file_1_data, file_2_data
