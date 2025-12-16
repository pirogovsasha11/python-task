import math

def square():
    x = float(input("Сторона квадрата: "))
    value = x * x
    result = math.ceil(value) \
        if not x.is_integer() \
        else int(value)
    print(f"Площадь квадрата: {result}")
    return result

area = square()