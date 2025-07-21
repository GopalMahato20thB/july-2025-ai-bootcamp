#12. grade_checker.py: Assign grades based on marks.
student_name = input("Enter Your name: ")
student_marks = float(input("Enter your marks: "))

if student_marks < 50:
    print(f"{student_name}: FAILED!") 
if student_marks >= 50 and student_marks < 60:
    print(f"{student_name}: D ")
if student_marks >= 60 and student_marks < 70:
    print(f"{student_name}: C ")
if student_marks >= 70 and student_marks < 80:
    print(f"{student_name}: B ") 
if student_marks >= 80 and student_marks < 90:
    print(f"{student_name}: A ")    
if student_marks >= 90 and student_marks <= 100:
    print(f"{student_name}: AA ")
    
