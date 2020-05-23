"""
def calculate_cost_of_travel(person_number):
    if person_number > 5:
        return person_number * 260
    return person_number * 300
print(calculate_cost_of_travel(2))
"""
def calculate_discount(account_tyle,money):
    if account_tyle == "vip":
        if money <= 500:
            return 0.85
        return 0.8
    else:
        if money >= 800:
            return 0.9
        return 1

print(calculate_discount("不是vip",2))

