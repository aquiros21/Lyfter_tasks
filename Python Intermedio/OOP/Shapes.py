from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return self.radius * 3.14 * 2

    def calculate_area(self):
        return self.radius ** 2 * 3.14


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        return self.side * 4
    
    def calculate_area(self):
        return self.side ** 2
    

class Rectangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_perimeter(self):
        return (self.base * 2) + (self.height * 2)
    
    def calculate_area(self):
        return (self.base * self.height)


rectangle_measures = Rectangle(4,8)

print(rectangle_measures.calculate_area())
print(rectangle_measures.calculate_perimeter())