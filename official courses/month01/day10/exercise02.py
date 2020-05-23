def calculate_total_seconds(hour=0, minute=0, seconds=0):
    return hour * 3600 + minute * 60 + seconds


print(calculate_total_seconds(1, 1, 1))
print(calculate_total_seconds(minute=1, seconds=1))
print(calculate_total_seconds(1, seconds=1))
print(calculate_total_seconds(minute=1))
