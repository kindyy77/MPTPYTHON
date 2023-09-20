import math
a = 0
b = 0

while True:
    print("Выберите действие : ")
    print("1. Сложение")
    print("2. Вычитание ")
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
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        c = a + b
        print(a,"+",b,"=",c)
    elif choice == "2":
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        c = a - b
        print(a, "-", b, "=", c)
    elif choice == "3":
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        c = a * b
        print(a, "*", b, "=", c)
    elif choice == "4" :
        a = int(input("Введите первое число : "))
        b = int(input("Введите второе число : "))
        c = a / b
        print(a, ":", b, "=", c)
    elif choice == "5" :
        a = int(input("Введите первое число : "))
        b = int(input("Введите степень : "))
        c = a ** b
        print(a, " в степени ", b, "=", c)
    elif choice == "6":
        a = int(input("Введите число : "))
        c = a ** 0.5
        print("Квадратный корень из ",a," = ",c)
    elif choice == "7" :
        a = int(input("Введите число : "))
        c = math.factorial(a)
        print("Факториал из ", a, " = ", c)
    elif choice == "8" :
        a = int(input("Введите число : "))
        b = math.radians(a)
        c = math.sin(b)
        print("Синус из ", a, " градусов = ", c)
    elif choice == "9" :
        a = int(input("Введите число : "))
        b = math.radians(a)
        c = math.cos(b)
        print("Косинус из", a, " градусов = ", c)
    elif choice == "10" :
        a = int(input("Введите число : "))
        b = math.radians(a)
        c = math.tan(b)
        print("Тангенс из", a, " градусов = ", c)
    elif choice == "11":
         print("Суицид...")
         break
    else:
         print("Неверный выбор. Попробуйте снова.")