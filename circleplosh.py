class Circle:
    @staticmethod
    def poisk_s(r):
        return 3.14 * r**7

r = 65
ploschads = Circle.poisk_s(r)
print(f"Площадь круга равна: {ploschads}")