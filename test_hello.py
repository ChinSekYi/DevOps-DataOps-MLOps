from hello import hi, bye


def test_hi():
    assert "hi" == hi()


def test_hi2():
    assert "bye" == bye()
