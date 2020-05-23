def calculate_multiplicative(*args):
    result = 1
    for number in args:
        result *= number
    return result

print(calculate_multiplicative(1,2,3,4,5,6))
