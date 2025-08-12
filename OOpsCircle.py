class Circle():
    pr = 3.14
    def __init__(self,r=1):
        self.radius = r
        self.area = r*r*Circle.pr
    def circumference(self):
        return self.radius*self.pr*2

my_circle = Circle()
print(my_circle.circumference())
my_circle2 = Circle(10)
print(my_circle2.circumference())