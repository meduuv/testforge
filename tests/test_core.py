from testforge.core import cases

def test_cases():
    assert cases(["a", "b"]) == [(1, "a"), (2, "b")]
