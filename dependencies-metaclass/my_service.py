import random
from singleton import SingletonMeta


class MyService(metaclass=SingletonMeta):
    def __init__(self):
        self._numbers = (0, 0)

    def update(self):
        self._numbers = (random.randint(1, 100), random.randint(1, 100))
        print(f"Updated numbers to {self._numbers}  {self.numbers}")

    @property
    def numbers(self):
        return self._numbers
