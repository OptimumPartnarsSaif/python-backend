import math

# Base class
class Shape:
    def __init__(self, name):
        self._name = name  # protected attribute

    def area(self):
        raise NotImplementedError("Subclasses must implement area method.")

    def __str__(self):
        return f"{self._name} with area {self.area():.2f}"

    def __add__(self, other):
        if isinstance(other, Shape):
            total_area = self.area() + other.area()
            return f"Combined area: {total_area:.2f}"
        return NotImplemented


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


# Interactive menu
def main():
    shapes = []
    while True:
        print("\nShape Menu:")
        print("1. Create Circle")
        print("2. Create Rectangle")
        print("3. Show all shapes")
        print("4. Add areas of two shapes")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            radius = float(input("Enter radius: "))
            shapes.append(Circle(radius))
            print("Circle created successfully.")

        elif choice == "2":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shapes.append(Rectangle(width, height))
            print("Rectangle created successfully.")

        elif choice == "3":
            if not shapes:
                print("No shapes created yet.")
            else:
                for i, shape in enumerate(shapes):
                    print(f"{i}: {shape}")

        elif choice == "4":
            if len(shapes) < 2:
                print("Need at least 2 shapes to add areas.")
            else:
                idx1 = int(input("Enter index of first shape: "))
                idx2 = int(input("Enter index of second shape: "))
                if 0 <= idx1 < len(shapes) and 0 <= idx2 < len(shapes):
                    print(shapes[idx1] + shapes[idx2])
                else:
                    print("Invalid indices.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
