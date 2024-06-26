def zamena_resultata(zamena):
    def decorator(func):
        def wrapper(*args, **kwargs):
            resultat = func(*args, **kwargs)
            return zamena
        return wrapper
    return decorator

@zamena_resultata("Результат заменен")
def dobavka_for_zameni(a, b):
    return a + b

resultat = dobavka_for_zameni(187, 78)
print(resultat)