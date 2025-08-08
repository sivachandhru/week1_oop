from math import pi
from dataclasses import dataclass

@dataclass
class Circle:
    radius: float
    def area(self) -> float:
        return pi * self.radius ** 2

@dataclass
class Rectangle:
    width: float
    height: float
    def area(self) -> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
