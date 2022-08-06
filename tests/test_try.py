from ernieproject.lib import try_me

def test_sum():
    num = try_me(3, 4)[0]
    assert num == 7