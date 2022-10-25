file_1_path = pathlib.Path.cwd().joinpath("tests/fixtures/file1_nested.json")
file_2_path = pathlib.Path.cwd().joinpath("tests/fixtures/file2_nested.json")

with open(file_1_path, "r") as file_1, open(file_2_path, "r") as file_2:
    file_1_dict, file_2_dict = json.load(file_1), json.load(file_2)


# print(file_1_dict)
# print(json.dumps(file_1_dict))

# TODO create types for nodes
# TODO create functions that will help to create nodes


def create_node(node):
    if is_leaf():
        pass


def check_status(node_1, node_2, key):
    pass
