class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def find_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

    def display(self):
        print("A polygon is a flat two-dimensional shape with straight sides that are fully closed.")


class Triangle(Polygon):

    def display(self):
        print("Triangles are shapes with three straight sides.")
        super().display()


class Square(Polygon):

    def display(self):
        print("Square are shapes with 4 straight sides.")
        super().display()


class Rectangle(Polygon):

    def display(self):
        print("Rectangle are shapes with 4 straight sides.")
        super().display()
