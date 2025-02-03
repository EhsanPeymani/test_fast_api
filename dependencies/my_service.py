import random


class MyService:
    def __init__(self):
        self._numbers = (0, 0)

    def update(self):
        self._numbers = (random.randint(1, 100), random.randint(1, 100))
        print(f"Updated numbers to {self._numbers}")

    @property
    def numbers(self):
        return self._numbers
