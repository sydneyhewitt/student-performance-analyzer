# Name: Sydney Hewitt
# Period: AM
# Student Performance Analyzer

# Program introduction
print("========================================")
print("      STUDENT PERFORMANCE ANALYZER")
print("========================================")
print(" ")
print("Enter the student's information below. ")
print(" ")

# Gathering Information
name = input("What is the student's name? ")        # Ask the user for the students name
grade = int(input("What grade level is the student in? "))      # Ask the user what grade the student is in
assignment_average = float(input("What is the student's assignment average? "))     # Asks the user what the student's assignment average is
quiz_average = float(input("What is the student's quiz average? "))     # Asks the user what the students quiz average is
test_average = float(input("What is the student's test average? "))     # Asks the user what the students test average is
attendance = float(input("What is the student's attendance percentage? "))      # Asks the user what the students attendence percentage is
missing = int(input("How many missing assignments does the student have? "))        # Asks the user how many missing assignments the student has
print(" ")

# Calculate Overall Grade
def calculate_grade(assignment_average, quiz_average, test_average):        # Calculates the students overall grade using the students test, assignment, and quiz averages

    assignment_portion = assignment_average * 0.30
    quiz_portion = quiz_average * 0.30
    test_portion = test_average * 0.40

    overall_grade = assignment_portion + quiz_portion + test_portion

    return overall_grade        # Return the variable overall_grade so that it can be stored outside the function

overall_grade = calculate_grade(assignment_average, quiz_average, test_average)     # Store the variable overall_grade outside the function

# Letter Grade
def letter_grade(overall_grade):        # Determines the students letter grade using conditional statements
    if overall_grade >= 90:
        print("Letter Grade: A")
    elif overall_grade >= 80:
        print("Letter Grade: B")
    elif overall_grade >= 70:
        print("Letter Grade: C")
    elif overall_grade >= 60:
        print("Letter Grade: D")
    else:
        print("Letter Grade: F")

# Attendance
def attendance_status(attendance):      # Determines the students attendence status using conditional statements
    if attendance >= 95:
        print("Excellent Attendance")
    elif attendance >= 90:
        print("Good Attendance")
    elif attendance >= 80:
        print("Attendance Warning")
    elif attendance < 80:
        print("Poor Attendance")

    print("Attendance Status: " + attendance_status(attendance))

# Assignment Status
def assignment_status(missing_assignments):     # Determines the students missing assignments status using conditional statements
    if missing_assignments == 0:
        print("Excellent")
    elif missing_assignments <= 2:
        print("Good")
    elif missing_assignments <= 4:
        print("Warning")
    elif missing_assignments >= 5:
        print("Critical")

    print("Missing Assignment Status: " + assignment_status(missing))

# Check eligibility
def check_eligibility(overall_grade, attendance, missing_assignments):      # Checks the students academic eligibility using nested conditional statements
    if overall_grade >= 70:
        if attendance >= 90:
            if missing_assignments <= 2:
                print("Academic Eligibility: ELIGIBLE")
                print("Student passed all three requirements.")
            else:
                print("Academic Eligibility: NOT ELIGIBLE")
                print("Reason: Too many missing assignments.")
        else: 
            print("Academic Eligibility: NOT ELIGIBLE")
            print("Reason: Attendance is too low.")
    else:
        print("Academic Eligibility: NOT ELIGIBLE")
        print("Reason: Overall grade is too low.")

# High Honors
def check_high_honors(overall_grade, attendance, missing_assignments):      # Checks if the student is high honors using nested conditional statements
    if overall_grade >= 90:
        if attendance >= 95:
            if missing_assignments == 0:
                print("High Honors: YES")
            else:
                print("High Honors: NO")
                print("Reason: Student has missing assignments.")
        else:
            print("High Honors: NO")
            print("Reason: Attendance requirement not met.")
    else:
        print("High Honors: NO")
        print("Reason: Grade requirement not met.")

# Good Standing
def check_good_standing(overall_grade, attendance):     # Checks if the student is in good standing using conditional statments
    if overall_grade >= 70 and attendance >= 90:
        print("Good Standing: YES")
    else:
        print("Good Standing: NO")

# Check Support
def check_support(overall_grade, attendance):       # Checks if the student need additional support using conditional statements
    if overall_grade < 70 or attendance < 80:
        print("Additional Support: RECOMMENDED")
    else:
        print("Additional Support: NOT NEEDED")

# Student Login

username = input("Enter username: ")        # Asks the user for the username for the login
pin = input("Enter PIN: ")      # Asks the user for the PIN for the login

def student_login(username, pin):       # Checks login to determine if whats typed is valid
    if username == "student":
        if pin == "1234":
            print("Login Successful!")
        else:
            print("Login Failed: Incorrect PIN.")
    else:
        print("Login Failed: Incorrect username.")

# Grade Level Message
def grade_level_message(grade_level):       # Writes a message based on the students grade level
    if grade_level == 9:
        print("Welcome to your freshman year!")
    elif grade_level == 10:
        print("Keep building your skills!")
    elif grade_level == 11:
        print("Junior year — keep pushing!")
    elif grade_level == 12:
        print("Senior year — finish strong!")
    else:
        print("Invalid grade level.")

# Strongest Academic Category
def strongest_category(assignment_average, quiz_average, test_average):     # Determines the students strongest category in school between tests, quizzes, and assignments
    if assignment_average > quiz_average and assignment_average > test_average:
        print("Strongest Category: Assignments")
    elif quiz_average > assignment_average and quiz_average > test_average:
        print("Strongest Category: Quizzes")
    elif test_average > quiz_average and test_average > assignment_average:
        print("Strongest Category: Tests")

# Check Advanced Status
def check_advanced_status(overall_grade, attendance, missing_assignments):      # Checks if the student is outstanding or standard status using conditional statements
    if (overall_grade >= 90 and attendance >= 95) or (overall_grade >= 85 and missing_assignments == 0):
        print("Advanced Status: OUTSTANDING STUDENT")
    else:
        print("Advanced Status: STANDARD STUDENT STATUS")

# Final Student Summary

student_login(username, pin)
print(" ")
print("----------- STUDENT SUMMARY -----------")
print(" ")
print("Student: " + name)
print("Grade Level: " + str(grade))
grade_level_message(grade)
print(" ")
print("Overall Grade: " + str(calculate_grade(assignment_average, quiz_average, test_average)))
print("Assignment Average: " + str(assignment_average))
print("Quiz Average: " + str(quiz_average))
print("Test Average: " + str(test_average))
letter_grade(overall_grade)
print(" ")
calculate_grade(assignment_average, quiz_average, test_average)
print("Attendance: " + str(attendance))
print("Missing Assignments: " + str(missing))
print(" ")
strongest_category(assignment_average, quiz_average, test_average)
print(" ")
check_eligibility(overall_grade, attendance, missing)
check_good_standing(overall_grade, attendance)
check_high_honors(overall_grade, attendance, missing)
check_support(overall_grade, attendance)
print(" ")
check_advanced_status(overall_grade, attendance, missing)
print(" ")
print("----------------------------------------")