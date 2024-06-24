class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def ploschads(self):
        return self.width * self.height


pryamougol = Rectangle(87, 9)
print(pryamougol.ploschads)