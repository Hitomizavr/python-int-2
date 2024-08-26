# Изначально тип float
a = float(input("Введите первую сторону прямоугольника: "));
b = float(input("Введите вторую сторону прямоугольника: "));

# Площадь прямоугольника
S = a * b;

# Периметр прямоугольника
P = (a + b) * 2;

# Если число целое - то меняем тип на int, иначе - float
def formatNumber(num):
    if num.is_integer():
        return int(num);
    return num;

print("Площадь прямоугольника:", formatNumber(S), "Периметр прямоугольника:", formatNumber(P));