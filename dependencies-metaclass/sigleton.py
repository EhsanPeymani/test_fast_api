class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


def test_signleton():
    class SingletonTest(metaclass=SingletonMeta):
        def __init__(self, value):
            self.value = value

    a = SingletonTest(10)
    b = SingletonTest(20)

    assert a is b
    assert a.value == 10
    assert b.value == 10
