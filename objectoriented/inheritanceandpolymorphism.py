class Shape():
    def area(self):
        raise NotImplementedError()
    def dispaly(self):
        raise NotImplementedError()
class Circle(Shape):
    def __init__(self,r):
        self.r = r 
    def area(self):
        self.area = 3.142 * self.r * self.r 
    
    def perimeter(self):
       self.perimeter = 2 * 3.142 * self.r

    def display(self):
        print("Area of Circle is:",self.area)

    def display(self):
        print("Perimeter of Circle is:",self.perimeter)

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        self.area = self.length * self.width

    def perimeter(self):
         self.perimeter = 2 * (self.length + self.width)

    def display(self):
        print("Area of Rectangle is:",self.area)
    
    def display(self):
        print("Perimeter of Rectangle is:",self.perimeter)

cir = Circle(3)
cir.area()
cir.perimeter()
cir.display()

rec = Rectangle(3,4)
rec.area()
rec.perimeter()
rec.display()