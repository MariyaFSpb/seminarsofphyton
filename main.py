def power(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * power(base, exp - 1))
base = int(input("Введите первое число: "))
exp = int(input("Введите второе число: "))
print("Результат возведения в степень равен:", power(base, exp))