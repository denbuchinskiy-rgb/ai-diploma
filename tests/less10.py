def invert_dict(d: dict) -> dict:
    inv = {}
    for k, v in d.items():
        inv[v] = k
    return inv

def get_nested(d: dict, path: list[str], default=None):
    cur = d
    for key in path:
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur

def merge_dicts(a: dict, b: dict, c: dict) -> dict:
    out=dict(a)
    out.update(b)
    out.update(c)
    return out
print(merge_dicts({"малина": 3}, {"малина": 2, "клубника": 3}, {"арбуз":1}))

def run_all_tests():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}

    data = {"a":{"b":{"c": 5}}}
    assert get_nested(data, ["a","b","c"]) == 5
    assert get_nested(data, ["a", "x"], default=0) == 0

    print ("✅ LESSON 10: all tests passed")

run_all_tests()