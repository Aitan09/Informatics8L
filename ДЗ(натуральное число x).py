import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

x = int(input("Введите число: "))
if is_prime(x):
    print("Число является простым")
else:
    print("Число не является простым")

