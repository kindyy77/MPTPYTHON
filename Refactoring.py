import math

def slojenie():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a + b
        print(a,"+",b,"=",c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def vichitanie():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a - b
        print(a, "-", b, "=", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def umnojenie():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        c = a * b
        print(a, "*", b, "=", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def delenye():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))
        if b != 0:
            c = a / b
            print(a, ":", b, "=", c)
        else:
            print("Деление на 0 невозможно")
    except ValueError:
        print("Неверный ввод. Введите число.")

def stepen():
    try:
        a = int(input("Введите первое число: "))
        b = int(input("Введите степень: "))
        c = a ** b
        print(a, "в степени", b, "=", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def qoren():
    try:
        a = int(input("Введите число: "))
        c = math.sqrt(a)
        print("Квадратный корень из", a, "=", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def factorial():
    try:
        a = int(input("Введите число: "))
        c = math.factorial(a)
        print("Факториал из", a, "=", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def sin():
    try:
        a = int(input("Введите число: "))
        b = math.radians(a)
        c = math.sin(b)
        print("Синус из", a, "градусов =", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def cos():
    try:
        a = int(input("Введите число: "))
        b = math.radians(a)
        c = math.cos(b)
        print("Косинус из", a, "градусов =", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def tangens():
    try:
        a = int(input("Введите число: "))
        b = math.radians(a)
        c = math.tan(b)
        print("Тангенс из", a, "градусов =", c)
    except ValueError:
        print("Неверный ввод. Введите число.")

def vihod():
    print("Суицид...")

while True:
    print("Выберите действие: ")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("5. Степень")
    print("6. Квадратный корень")
    print("7. Факториал")
    print("8. Синус")
    print("9. Косинус")
    print("10. Тангенс")
    print("11. Отчисление")

    choice = str(input("Выберите пункт меню: "))

    if choice == "1":
        slojenie()
    elif choice == "2":
        vichitanie()
    elif choice == "3":
        umnojenie()
    elif choice == "4":
        delenye()
    elif choice == "5":
        stepen()
    elif choice == "6":
        qoren()
    elif choice == "7":
        factorial()
    elif choice == "8":
        sin()
    elif choice == "9":
        cos()
    elif choice == "10":
        tangens()
    elif choice == "11":
        vihod()
        break
    else:
        print("Неверный ввод. Введите число.")