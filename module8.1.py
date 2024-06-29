def add_everything_up(a, b):
    try:
        # Попытка сложить a и b как числа
        return a + b
    except TypeError:
        # Если возникла ошибка типа, значит a и b разных типов
        # Возвращаю строковое представление этих двух данных вместе
        # return f"{a}{b}"
        return str(a) + str(b)

# Примеры использования функции
print(add_everything_up(123.456,'строка'))
print(add_everything_up('яблоко',4215))
print(add_everything_up(123.456, 7))