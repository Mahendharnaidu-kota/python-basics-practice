# Grade Calculator
s1 = float(input("Enter subject 1 marks : "))
s2 = float(input("Enter subject 2 marks : "))
s3 = float(input("Enter subject 3 marks : "))
s4 = float(input("Enter subject 4 marks : "))
s5 = float(input("Enter subject 5 marks : "))

valid = True

if s1 < 0 or s1 > 100:
    valid = False
if s2 < 0 or s2 > 100:
    valid = False
if s3 < 0 or s3 > 100:
    valid = False
if s4 < 0 or s4 > 100:
    valid = False
if s5 < 0 or s5 > 100:
    valid = False

if valid == False:
    print("Invalid input. Each subject's marks must be between 0 - 100")
else:
    total_marks_obtained = s1 + s2 + s3 + s4 + s5
    total_marks = 500

    if total_marks_obtained > 450:
        grade = "A"
    elif total_marks_obtained > 400:
        grade = "B"
    elif total_marks_obtained > 350:
        grade = "C"
    elif total_marks_obtained > 300:
        grade = "D"
    elif total_marks_obtained > 250:
        grade = "E"
    else:
        grade = "F"
    
    if grade == "A":
        gpa = 4.0
    elif grade == "B":
        gpa = 3.0
    elif grade == "C":
        gpa = 2.0
    elif grade == "D":
        gpa = 1.0
    elif grade == "E":
        gpa = 0.5
    else:
        gpa = 0.0

    if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E":
        deter = "Pass"
    else:
        deter = "Fail"

    print("*" * 50)
    print("---Grade Calculator---")
    print(f"Exam conducted for {total_marks} marks")
    print(f"Total marks obtained is {total_marks_obtained}")
    print(f"Grade is {grade}")
    print(f"GPA is {gpa}")
    print(f"determination = {deter}")
    print("*" * 50)