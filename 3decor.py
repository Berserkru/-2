def preobraz(func):
    def wrapper(*args, **kwargs):
        resultat = func(*args, **kwargs)
        return str(resultat)
    return wrapper

@preobraz
def plus(a, b):
    return a + b

resultat = plus(100, 48)
print(f" {resultat} Белград, тип данных: {type(resultat)}")