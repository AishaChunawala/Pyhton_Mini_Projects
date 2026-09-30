num_students = int(input("Enter the number of students to know the minimum number of benches needed: "))
if num_students % 2 == 0:
    print(f"The minimum number of benches needed is: {num_students / 2}")
else:
    print(f"The minimum number of benches needed is: {num_students // 2 + 1}")