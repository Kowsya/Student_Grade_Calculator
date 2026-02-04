def Calculate_grade(marks):
    if not marks:
        return "No marks provided"
    
    # Check if any marks are outside the valid range (0-100)
    if any(m < 0 or m > 100 for m in marks):
        return "Invalid marks detected"
    
    average = sum(marks) / len(marks)

    # Detailed Grading Scale
    if average >= 90: return "A+"
    if average >= 80: return "A"
    if average >= 70: return "B+"
    if average >= 60: return "B"
    if average >= 50: return "C"
    if average >= 40: return "D"
    return "Fail"

if __name__ == "__main__":
    user_marks = []
    print("--- Student Grade Calculator ---")
    try:
        for i in range(1, 6):
            m = float(input(f"Enter marks for subject {i} (0-100): "))
            # Condition: Validation check during input
            if m < 0 or m > 100:
                print("Error: Marks must be between 0 and 100.")
                exit() # Stop the program if input is bad
            user_marks.append(m)

        result = Calculate_grade(user_marks)
        print(f"\nAverage: {sum(user_marks)/len(user_marks):.2f}")
        print("Final Grade:", result)
        
    except ValueError:
        print("Error: Please enter numbers only.")