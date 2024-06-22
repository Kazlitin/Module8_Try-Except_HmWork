def add_everything_up(a, b):
    # Проверяю типы аргументов
    if isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return f"{a} {b}"

print(add_everything_up("Hello", "World"))
print(add_everything_up(10, 20))
print(add_everything_up("10", "20"))
print(add_everything_up(10, "20"))
print(add_everything_up("10", 20))