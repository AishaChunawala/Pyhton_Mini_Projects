import math

a = int(input("Enter students in Class 1: "))
b = int(input("Enter students in Class 2: "))
c = int(input("Enter students in Class 3: "))

desks1 = math.ceil(a / 2)
desks2 = math.ceil(b / 2)
desks3 = math.ceil(c / 2)

total_desks = desks1 + desks2 + desks3

print(f"Minimum number of desks = {total_desks}")
