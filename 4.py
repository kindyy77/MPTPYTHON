number = int(input("Введите число : "))
def sum_digits(number):
    return sum(int(digit) for digit in str(number))
print(sum_digits(number))