class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        x = self.length * self.width
        print(x)
    def perimeter(self):
        x =(self.length * 2) + (self.width*2)
        print(x)

class Square(Rectangle):
    def __init__(self,length):
        self.length=length
        self.width=length



rect = Rectangle(2, 4)
rect.area()
# 8

square = Square(8)
square.area()
# 64

square.perimeter()
# 32