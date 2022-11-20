from gendiff import deserialize_files_to_dict, generate_diff
from gendiff.formatters import format_stylish


def test_flat_json():
    expected_result = (
        "{\n\t-  follow: false\n\t   host: hexlet.io\n\t-  proxy: 123.234.53.22\n\t-  timeout: 50\n\t+  "
        "timeout: 20\n\t+  verbose: true\n}"
    )
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_flat.json", "tests/fixtures/file2_flat.json"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_stylish(diff)
    assert result == expected_result


def test_flat_yaml():
    expected_result = (
        "{\n\t-  follow: false\n\t   host: hexlet.io\n\t-  proxy: 123.234.53.22\n\t-  timeout: 50\n\t+  "
        "timeout: 20\n\t+  verbose: true\n}"
    )
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_flat.yml", "tests/fixtures/file2_flat.yml"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_stylish(diff)
    assert result == expected_result


def test_nested_json():
    expected_result = (
        "{\n\tcommon: {\n\t\t+  follow: false\n\t\t   setting1: Value 1\n\t\t-  setting2: 200\n\t\t-  "
        "setting3: true\n\t\t+  setting3: null\n\t\t+  setting4: blah blah\n\t\tsetting5: {\n\t\t\t+  "
        "key5: value5\n\t\t}\n\t\tsetting6: {\n\t\t\tdoge: {\n\t\t\t\t-  wow: \n\t\t\t\t+  wow: so "
        "much\n\t\t\t}\n\t\t\t   key: value\n\t\t\t+  ops: vops\n\t\t}\n\t}\n\tgroup1: {\n\t\t-  baz: "
        "bas\n\t\t+  baz: bars\n\t\t   foo: bar\n\t\t-  nest: {\n\t\t\tkey: value\n\t\t}\n\t\t+  nest: "
        "str\n\t}\n\t-  group2: {\n\t\tabc: 12345\n\t\tdeep: {\n\t\t\tid: 45\n\t\t}\n\t}\n\tgroup3: {"
        "\n\t\tdeep: {\n\t\t\tid: {\n\t\t\t\t+  number: 45\n\t\t\t}\n\t\t}\n\t\t+  fee: 100500\n\t}\n}"
    )
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_nested.json", "tests/fixtures/file2_nested.json"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_stylish(diff)
    assert result == expected_result


def test_nested_yaml():
    expected_result = (
        "{\n\tcommon: {\n\t\t+  follow: false\n\t\t   setting1: Value 1\n\t\t-  setting2: 200\n\t\t-  "
        "setting3: true\n\t\t+  setting3: null\n\t\t+  setting4: blah blah\n\t\tsetting5: {\n\t\t\t+  "
        "key5: value5\n\t\t}\n\t\tsetting6: {\n\t\t\tdoge: {\n\t\t\t\t-  wow: \n\t\t\t\t+  wow: so "
        "much\n\t\t\t}\n\t\t\t   key: value\n\t\t\t+  ops: vops\n\t\t}\n\t}\n\tgroup1: {\n\t\t-  baz: "
        "bas\n\t\t+  baz: bars\n\t\t   foo: bar\n\t\t-  nest: {\n\t\t\tkey: value\n\t\t}\n\t\t+  nest: "
        "str\n\t}\n\t-  group2: {\n\t\tabc: 12345\n\t\tdeep: {\n\t\t\tid: 45\n\t\t}\n\t}\n\tgroup3: {"
        "\n\t\tdeep: {\n\t\t\tid: {\n\t\t\t\t+  number: 45\n\t\t\t}\n\t\t}\n\t\t+  fee: 100500\n\t}\n}"
    )
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_nested.json", "tests/fixtures/file2_nested.json"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_stylish(diff)
    assert result == expected_result
