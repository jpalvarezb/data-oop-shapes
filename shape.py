# pylint: disable=too-few-public-methods missing-module-docstring
class Shape:
    '''General shape class'''
    def __init__(self, color, name):
        '''Initialize shape class'''
        self.color = color
        self.name = name
    def say_name(self):
        '''Say name function for unspecified shapes'''
        return f'My name is {self.name}.'
class Rectangle(Shape):
    '''Rectangle sub-class'''
    def __init__(self, color, name, width, height):
        '''Inheriting self, color, and name from shape class'''
        super().__init__(color, name)
        self.width = width
        self.height = height
    def say_name(self):
        '''Say name function for rectangle shapes'''
        return f'My name is {self.name} and I am a rectangle.'
    def area(self):
        '''Area function for rectangle shapes'''
        return self.width * self.height
    def perimeter(self):
        '''Perimeter function for rectangle shapes'''
        return 2 * (self.width + self.height)
class Circle(Shape):
    '''Circle sub-class'''
    def __init__(self, color, name, radius):
        '''Inheriting self, color, and name from shape class'''
        super().__init__(color, name)
        self.radius = radius
    def say_name(self):
        '''Say name function for circle shapes'''
        return f'My name is {self.name} and I am a circle.'
    def area(self):
        '''Area function for circle shapes'''
        return 3.14 * self.radius ** 2
    def perimeter(self):
        '''Perimeter function for circle shapes'''
        return 2 * 3.14 * self.radius
