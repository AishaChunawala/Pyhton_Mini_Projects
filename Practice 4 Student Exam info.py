name = input("Enter your name: ")
subject_1 = float(input("Enter your marks for Subject 1: "))
subject_2 = float(input("Enter your marks for Subject 2: "))
subject_3 = float(input("Enter your marks for Subject 3: "))
total_marks = subject_1 + subject_2 + subject_3
avg_marks = total_marks / 3
# Display the result
print(f"The name of student is {name}, total marks scored is {total_marks} and average mark is {avg_marks}.")
