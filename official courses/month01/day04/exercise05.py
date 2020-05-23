total_value = 0
for number in range(10, 61):
    if number % 10 == 3 or number % 10 == 5 or number % 10 == 8:
        continue
    total_value += number
print(total_value)
