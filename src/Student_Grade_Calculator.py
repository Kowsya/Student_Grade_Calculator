def Calculate_grade(marks):
    if not marks:
        return "No marks provided"
    
    average = sum(marks)/ len(marks)

    if average >= 90:
      return "A+"
    elif average >= 75:
       return "A"
    elif average >= 60:
       return "B"
    elif average >= 50:
       return "C"
    else:
       return "Fail"
    
user_marks = []

for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    user_marks.append(m)

result = Calculate_grade(user_marks)
print("Final Grade:", result)