class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

rectangle = Rectangle(8, 3)
print("Area Of Rectangle:", rectangle.area())  # Output: Area: 24
print("Perimeter Of Rectangle:", rectangle.perimeter())  # Output: Perimeter: 22
