import math

# Base class
class Shape:
    def __init__(self, name):
        self._name = name  # protected attribute

    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

    def __str__(self):
        return f"{self._name} with area {self.area():.2f}"


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.__radius = radius  # private attribute

    def area(self):
        return math.pi * self.__radius ** 2


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape)  # Calls __str__ for each
