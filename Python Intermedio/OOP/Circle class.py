class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius ** 2 * 3.14


c = Circle(5)

print(c.radius)
print(c.get_area())
