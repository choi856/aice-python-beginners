total_books = 620
student_per_group = 5 

completed_shares = total_books // student_per_group
leftovers = total_books % student_per_group

print(f"full group : {completed_shares}")
print(f"leftover books : {leftovers}")

student_id = 2027

if student_id % 2 == 0:
    print(f"Student ID {student_id} is even.")
else:
    print(f"Student ID {student_id} is odd.")
