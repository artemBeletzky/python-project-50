from gendiff import parse_file_to_dict, generate_diff


def test_flat_json():
    expected_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    dict_1, dict_2 = parse_file_to_dict(
        "tests/fixtures/file1_flat.json", "tests/fixtures/file2_flat.json"
    )
    result = generate_diff(dict_1, dict_2)
    assert expected_result == result


# def test_flat_yaml():
#     expected_result = """{
#   - follow: false
#     host: hexlet.io
#   - proxy: 123.234.53.22
#   - timeout: 50
#   + timeout: 20
#   + verbose: true
# }"""
#     dict_1, dict_2 = parse_file_to_dict(
#         "tests/fixtures/file1_flat.yml", "tests/fixtures/file2_flat.yml"
#     )
#     result = generate_diff(dict_1, dict_2)
#     assert expected_result == result
