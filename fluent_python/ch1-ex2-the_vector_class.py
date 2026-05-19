import math
from typing import override

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @override
    def __repr__(self) -> str:
        # If you only implement one of the special methods __str__
        # __repr__, use the latter one as it is user-friendly and
        # Python calls it as a fallback special method.
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """Returns False if magnitude is zero, True otherwise"""
        return bool(abs(self))
        # return bool(self.x or self.y) # a faster but harder to read implementation

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    vector = Vector(3,5)
    print(vector)
    print(f'{abs(vector):.2f}')
    print(bool(vector))
