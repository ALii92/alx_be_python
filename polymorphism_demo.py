import math
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError ("derived classes need to override this method.")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return(f"{self.length * self.width}")
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return(f"{self.radius ** 2 * math.pi}")