import math
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


def calculate_total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)


if __name__ == "__main__":
    shapes: List[Shape] = [
        Square(4),
        Rectangle(3, 5),
        Circle(2)
    ]

    total_area = calculate_total_area(shapes)
    print(f"Total area of all shapes: {total_area:.2f}")