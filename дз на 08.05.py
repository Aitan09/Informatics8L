result = 4**3 * 3**19

result_trinary = ''
while result > 0:
    result_trinary = str(result % 3) + result_trinary
    result //= 3

count_zeros = result_trinary.count('0')

print(f"Количество символов '0' в троичной записи: {count_zeros}")
