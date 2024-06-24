def add_everything_up(a, b):
    try:
        return a + b
    except TypeError as e:
        # Если возникла ошибка типа, значит a и b разных типов
        # Возвращаю строковое представление этих двух данных вместе
        return f"{a} {b}"
print(add_everything_up(1, 2))  # Выведет: 3
print(add_everything_up("Hello", "World"))  # Выведет: "Hello World"
print(add_everything_up(1, "World"))  # Выведет: "1 World"
print(add_everything_up("Hello", 2))  # Выведет: "Hello 2"