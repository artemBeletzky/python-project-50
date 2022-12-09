from gendiff.gendiff import generate_diff


def test_flat_json_stylish():
    expected_result = (
        "'{\\n  - follow: false\\n    host: hexlet.io\\n  - proxy: 123.234.53.22\\n  "
        "- timeout: 50\\n  + timeout: 20\\n  + verbose: true\\n}'"
    )
    diff = generate_diff(
        "tests/fixtures/file1_flat.json", "tests/fixtures/file2_flat.json"
    )
    assert diff == expected_result


def test_flat_yaml_stylish():
    expected_result = (
        "'{\\n  - follow: false\\n    host: hexlet.io\\n  - proxy: 123.234.53.22\\n  "
        "- timeout: 50\\n  + timeout: 20\\n  + verbose: true\\n}'"
    )
    diff = generate_diff(
        "tests/fixtures/file1_flat.yml", "tests/fixtures/file2_flat.yml"
    )
    assert diff == expected_result


def test_nested_json_stylish():
    expected_result = (
        "'{\\n    common: {\\n      + follow: false\\n        setting1: Value "
        '1\\n      - setting2: 200\\n      - setting3: true\\n      + setting3: '
        'null\\n      + setting4: blah blah\\n      + setting5: {\\n            key5: '
        'value5\\n        }\\n        setting6: {\\n            doge: '
        '{\\n              - wow: \\n              + wow: so much\\n            '
        '}\\n            key: value\\n          + ops: vops\\n        }\\n    }\\n    '
        'group1: {\\n      - baz: bas\\n      + baz: bars\\n        foo: bar\\n      '
        '- nest: {\\n            key: value\\n        }\\n      + nest: str\\n    '
        '}\\n  - group2: {\\n        abc: 12345\\n        deep: {\\n            id: '
        '45\\n        }\\n    }\\n  + group3: {\\n        deep: {\\n            id: '
        '{\\n                number: 45\\n            }\\n        }\\n        fee: '
        "100500\\n    }\\n}'"
    )
    diff = generate_diff(
        "tests/fixtures/file1_nested.json", "tests/fixtures/file2_nested.json"
    )
    assert diff == expected_result


def test_nested_yaml_stylish():
    expected_result = (
        "'{\\n    common: {\\n      + follow: false\\n        setting1: Value "
        '1\\n      - setting2: 200\\n      - setting3: true\\n      + setting3: '
        'null\\n      + setting4: blah blah\\n      + setting5: {\\n            key5: '
        'value5\\n        }\\n        setting6: {\\n            doge: '
        '{\\n              - wow: \\n              + wow: so much\\n            '
        '}\\n            key: value\\n          + ops: vops\\n        }\\n    }\\n    '
        'group1: {\\n      - baz: bas\\n      + baz: bars\\n        foo: bar\\n      '
        '- nest: {\\n            key: value\\n        }\\n      + nest: str\\n    '
        '}\\n  - group2: {\\n        abc: 12345\\n        deep: {\\n            id: '
        '45\\n        }\\n    }\\n  + group3: {\\n        deep: {\\n            id: '
        '{\\n                number: 45\\n            }\\n        }\\n        fee: '
        "100500\\n    }\\n}'"
    )
    diff = generate_diff(
        "tests/fixtures/file1_nested.json", "tests/fixtures/file2_nested.json"
    )
    assert diff == expected_result

# TODO ADD TESTS FOR PLAIN
