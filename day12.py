"""based on https://github.com/nedbat/adventofcode2023/blob/main/new.py"""

import re
import pathlib
from dataclasses import dataclass
import json
from pprint import pprint

TEST_INPUT = """\
{"a":2,"b":4}
"""

FILE = pathlib.Path("day12_input.txt").read_text()


def parse_table(text: str) -> list[tuple[str, int]]:
    entries: list[tuple[str, int]] = []
    for line in text.splitlines():
        card, bid = line.split()
        entries.append((card, int(bid)))
    return entries


def part1(text: str) -> int:
    s = 0
    for line in text.splitlines():
        digits = re.findall(r"-?\d+", line)
        s += sum(int(x) for x in digits)
    return s


def test_part1():
    assert part1('{"a":2,"b":4}') == 6
    assert part1("[[[3]]]") == 3
    assert part1('[-1,{"a":1}]') == 0
    assert part1('{"a":{"b":4},"c":-1}') == 3
    assert part1("[]") == 0
    assert part1("{}") == 0


if __name__ == "__main__":
    answer = part1(FILE)
    print(answer)


def part2(text: str) -> int:
    json_object = json.loads(text)

    return sum_integers_in_json(json_object, ignored="red")


def sum_integers_in_json(obj: str, ignored: str = "") -> int:
    s = 0
    if isinstance(obj, dict):
        values = obj.values()
        if ignored not in values:
            for value in values:
                s += sum_integers_in_json(value, ignored=ignored)
    elif isinstance(obj, list):
        for item in obj:
            s += sum_integers_in_json(item, ignored=ignored)
    elif isinstance(obj, int):
        s += obj

    return s


def test_sum_integers_in_json():
    assert sum_integers_in_json(json.loads('{"a":2,"b":4}')) == 6
    assert sum_integers_in_json(json.loads("[[[3]]]")) == 3
    assert sum_integers_in_json(json.loads('[-1,{"a":1}]')) == 0
    assert sum_integers_in_json(json.loads('{"a":{"b":4},"c":-1}')) == 3
    assert sum_integers_in_json(json.loads('{"a":2,"b":4}')) == 6
    assert sum_integers_in_json(json.loads('{"a":2,"b":4}')) == 6
    assert sum_integers_in_json(json.loads("[]")) == 0
    assert sum_integers_in_json(json.loads("{}")) == 0


def test_part2():
    assert part2('{"a":2,"b":4}') == 6
    assert part2('[1,{"c":"red","b":2},3]') == 4
    assert part2('{"d":"red","e":[1,2,3,4],"f":5}') == 0
    assert part2('[1,"red",5]') == 6


if __name__ == "__main__":
    answer = part2(FILE)
    print(answer)
