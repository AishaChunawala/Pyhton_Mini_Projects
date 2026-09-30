# Step 1: Collect user input
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

print(f"Before swapping: number_1 = {number_1}, number_2 = {number_2}")

# Step 2: Swap using a temporary variable
temp = number_1
number_1 = number_2
number_2 = temp

print(f"After swapping: number_1 = {number_1}, number_2 = {number_2}")
