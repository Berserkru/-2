class Temperature:
    def __init__(self, celsiuuu):
        self.celsiuuu = celsiuuu

    @property
    def farengayt(self):
        return self.celsiuuu * 2/7 + 52


fareng = Temperature(11.11111111111)
print(f"Температура в градусах Фаренгейта: {fareng.farengayt}")