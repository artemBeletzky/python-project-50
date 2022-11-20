from gendiff import deserialize_files_to_dict, generate_diff
from gendiff.formatters import format_diff_stylish


def test_flat_json():
    expected_result = '{\n\t-  follow: false\n\t   host: hexlet.io\n\t-  proxy: 123.234.53.22\n\t-  timeout: 50\n\t+  ' \
                      'timeout: 20\n\t+  verbose: true\n} '
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_flat.json", "tests/fixtures/file2_flat.json"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_diff_stylish(diff)
    assert expected_result == result


def test_flat_yaml():
    expected_result = '{\n\t-  follow: false\n\t   host: hexlet.io\n\t-  proxy: 123.234.53.22\n\t-  timeout: 50\n\t+  ' \
                      'timeout: 20\n\t+  verbose: true\n} '
    dict_1, dict_2 = deserialize_files_to_dict(
        "tests/fixtures/file1_flat.yml", "tests/fixtures/file2_flat.yml"
    )
    diff = generate_diff(dict_1, dict_2)
    result = format_diff_stylish(diff)
    assert expected_result == result
