def convert_to_decimal(number, base):
    
    decimal = 0
    power = 0
    while number > 0:
        decimal += (number % 10) * (base ** power)
        number //= 10
        power += 1
    return decimal

def calculate_expression_value(expression):

    decimal_expression = []
    for exp_tuple in expression:
        decimal = convert_to_decimal(int(exp_tuple[0], exp_tuple[1]), exp_tuple[1])
        decimal_expression.append(decimal)
    
    return decimal_expression[0] + decimal_expression[1] * decimal_expression[2] ** decimal_expression[3]

def count_H_occurrences(value):
 
    count = str(value).count('H')
    return count


expression = [
    ("105", 8),
    ("5F", 35),
    ("1011", 3),
    ("BA", 15)
]


result = calculate_expression_value(expression)


count_H = count_H_occurrences(result)

print(f"Количество букв 'H' в значении выражения: {count_H}")
