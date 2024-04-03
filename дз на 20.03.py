def average(*args):
    if not args:
        return None

    total = 0
    count = 0

    for arg in args:
        try:
            total += arg
            count += 1
        except TypeError:
            pass

    if count == 0:
        return None

    return total / count
result = average(1, 2, 3, 4, 5)
print(result)  
