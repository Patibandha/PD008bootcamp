from newcal import add


def test_add():
    res = add("%%%%%", 40)
    assert res == 60
