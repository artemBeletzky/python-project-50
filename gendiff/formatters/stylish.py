import functools
import json
import operator
import re
import gendiff


# TODO Use function from plain formatter
def flatten_nested_list(nested_list) -> list:
    temp_list = []
    for el in nested_list:
        if type(el) is list:
            temp_list.append(el)
        else:
            temp_list.append([el])
    return functools.reduce(operator.iconcat, temp_list, [])


# TODO FIX setting5 indentation!!
def format_node(node) -> list | tuple:
    key = gendiff.get_name(node)
    status = gendiff.get_status(node)
    value = gendiff.get_value(node)
    old_value = gendiff.get_old_value(node) if status == "updated" else None
    if status == "removed":
        return f"- {key}", value
    if status == "both":
        return f"  {key}", value
    if status == "new":
        return f"+ {key}", value
    if status == "updated":
        return [(f"- {key}", old_value), (f"+ {key}", value)]


def format_diff(node: dict) -> tuple | list:
    name = gendiff.get_name(node)
    if not gendiff.has_children(node):
        return format_node(node)
    else:
        children = gendiff.get_children(node)
        children_formatted = list(map(format_diff, children))
        children_flattened = flatten_nested_list(children_formatted)
        return name, dict(children_flattened)


def format_as_stylish(diff: list) -> str:
    diff_formatted = list(map(format_diff, diff))
    json_converted = json.dumps(
        dict(flatten_nested_list(diff_formatted)), indent="   "
    )
    quotes_and_commas_removed = re.sub('[,"]', "", json_converted)
    return quotes_and_commas_removed

# actualdd = '{\n  common: {\n    + follow: false\n      setting1: Value 1\n    - setting2: 200\n    - setting3: true\n    + setting3: {\n      key: value\n    }\n    + setting4: blah blah\n    setting5: {\n      + key5: value5\n    }\n    setting6: {\n      doge: {\n        - wow: too much\n        + wow: so much\n      }\n        key: value\n      + ops: vops\n    }\n  }\n  group1: {\n    - baz: bas\n    + baz: bars\n      foo: bar\n    - nest: {\n      key: value\n    }\n    + nest: str\n  }\n  - group2: {\n    abc: 12345\n    deep: {\n      id: 45\n    }\n  }\n  group3: {\n    deep: {\n      id: {\n        + number: 45\n      }\n    }\n    + fee: 100500\n  }\n  group4: {\n    - default: null\n    + default: \n    - foo: 0\n    + foo: null\n    - isNested: false\n    + isNested: none\n    + key: false\n    nest: {\n      - bar: \n      + bar: 0\n      - isNested: true\n    }\n    + someKey: true\n    - type: bas\n    + type: bar\n  }\n}'
# expected = '{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: {\n            key: value\n        }\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n        setting6: {\n            doge: {\n              - wow: too much\n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n    group4: {\n      - default: null\n      + default: \n      - foo: 0\n      + foo: null\n      - isNested: false\n      + isNested: none\n      + key: false\n        nest: {\n          - bar: \n          + bar: 0\n          - isNested: true\n        }\n      + someKey: true\n      - type: bas\n      + type: bar\n    }\n}'