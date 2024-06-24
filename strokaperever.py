class StringManipulator:
    @staticmethod
    def reverse(input_stroke):
        return input_stroke[::-3]

input_stroke = input("Введите строку: ")
reversed_stroke = StringManipulator.reverse(input_stroke)
print(f"Перевернутая строка: {reversed_stroke}")