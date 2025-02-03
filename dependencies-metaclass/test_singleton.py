from singleton import SingletonMeta


def test_singleton():
    class SingletonTest(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value

    a = SingletonTest(10)
    b = SingletonTest(20)

    assert a is b
    assert a.value == 10
    assert b.value == 10
