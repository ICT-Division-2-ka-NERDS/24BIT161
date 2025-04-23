class Shape:
    def __init__(self):
        pass
    def perimeter(self):
        pass
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    
class square(Shape):
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return 4 * self.side
    def area(self):
        return self.side ** 2        
              
Shape1 = Rectangle(10, 5)
print("The perimeter and area of the rectangle with length=10 and breadth=5 are:")
print("Perimeter:")
print(Shape1.perimeter())
print("Area:")
print(Shape1.area())
Shape2 = Circle(7)
print('\n')
print("The perimeter and area of the circle with radius=7 are:")
print("Perimeter:")
print(Shape2.perimeter())
print("Area:")
print(Shape2.area())
Shape3 = square(10)
print('\n')
print("The perimeter and area of the square with side 10 are:")
print("Perimeter:")
print(Shape3.perimeter())
print("Area:")
print(Shape3.area())
