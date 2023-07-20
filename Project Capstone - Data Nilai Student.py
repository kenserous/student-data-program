# Purpose: Keep track of student's collective and individual data and academic performance
# Unique features other than required features:
    # Automatically sorted based on ID number, ascending order
    # Does not crash on invalid input
    # Features for pass rate and average grades
    # Easily updated
    # RP calculation system

# Improvements to be made:
    # Tabulation

student_data = [
    {'name':'Kenn','idNo':10001,'phy':51,'chem':24,'math':45,'econ':86},
    {'name':'Owen','idNo':10002,'phy':34,'chem':61,'math':89,'econ':58},
    {'name':'Jonathan','idNo':10003,'phy':91,'chem':87,'math':33,'econ':100}
] # Dummy data
student_id_list = [] # Dummy data 2
rank_points_data = {
    '70': 20,
    '60-69': 17.5,
    '55-59': 15,
    '50-54': 12.5,
    '45-49': 10,
    '40-44': 5,
    '0-39': 0
} # For rank point calculation
subName = {1: 'Physics', 2: 'Chemistry', 3: 'Mathematics', 4: 'Economics'} # For printing
subNameShort = {1: 'phy', 2: 'chem', 3: 'math', 4: 'econ'} # For extracting data from student_data
passGrade = 45 # Minimum Passing Grade

def intMenu(prompt): # To skip error codes from all inputs that require an integer input
    while True:
        try:
            value = int(input(prompt))
            return value
        except (ValueError, NameError):
            print("Something went wrong. Please input a valid number.")
            
def sortStudentData():
    global student_data
    student_data = sorted(student_data, key=lambda x: x['idNo']) # Always sort student_data
    # Creates list of all student IDs for use in other functions
    student_id_list.clear() # Clears the student_id_list so we can update the sorted student_data into the list.
    for i, student in enumerate(student_data):
        student_id_list.append(student['idNo'])
    # Since student_data will always be sorted, student_id_list will also be sorted accordingly.

def main_menu(): # Main Menu
    global menu
    global student_data
    sortStudentData()
    # Main Function
    print("==================================\n"
        "Student Marks Database\n"
        "Menu:\n"
        "1 - Students List\n"
        "2 - Add Student\n"
        "3 - Update Student\n"
        "4 - Remove Student\n"
        "5 - Statistics\n"
        "6 - Calculate Rank Points\n"
        "0 - Exit\n"
        "==================================")
    menu = intMenu("Input menu number: ")

def allStudentsData(i,y): # Displays all students' grades
    print("==================================\n"
        "Students Data\n"
        "No | ID No\t| Name\t\t| Physics | Chemistry   | Mathematics    | Economics\t|")
    for i in y:
         print(f"{i+1}  | {student_data[i]['idNo']}\t| {student_data[i]['name']}  \t| {student_data[i]['phy']}\t  |"
            f" {student_data[i]['chem']}\t\t| {student_data[i]['math']}\t\t |"
            f" {student_data[i]['econ']}   \t|")

def studentsList(): # Menu 1 Function
    while True:
        if len(student_data) == 0:
            print("No student data is available.")
            print("Please input at least one student data.")
            break
        else:
            print("==================================\n"
            "Students List Menu:\n"
            "1. Show all student data\n"
            "2. Input student ID\n"
            "3. Back to Main Menu\n"
            "==================================")
            student_menu = intMenu("Input menu number: ")
        if student_menu == 1: 
            allStudentsData(0,range(len(student_data))) # Displays data of all students
        elif student_menu == 2: # Displays data of one student
            input_id = intMenu("Enter the Student ID: ")
            while input_id not in student_id_list:
                print(f"Student ID {input_id} not found.")
                input_id = intMenu("Enter the Student ID: ")
            else:
                idIndex = student_id_list.index(input_id)
                # Index of student ID in sorted student_id_list, hence same index in student_data.
                allStudentsData(idIndex,range(idIndex,idIndex+1)) # Displays data of selected student
        elif student_menu == 3: break

def newStudent(): # Function to add new student to database
    while True:
        print("==================================\n"
        "New Student Menu:\n"
        "1. Add new student data\n"
        "2. Back to Main Menu\n"
        "==================================")
        new_menu = intMenu("Input menu number: ") 
        if new_menu == 1:
            print("Student ID has to be 5 numbers.")
            input_id = input("Input Student ID: ")
            while len(input_id) != 5 or input_id.isnumeric() == False:
                print("Student ID does not meet the conditions.")
                print("Please input another ID.")
                input_id = input("Input Student ID: ")
            else:
                studentID = int(input_id)
                if studentID in student_id_list: # Check for duplicate student ID in student_id_list.
                    print(f"{studentID} is already found in list.")
                else:
                    student_name = input("Student Name: ")
                    if student_name.isalpha(): 
                        phyGrade = intMenu("Physics marks: ")
                        chemGrade = intMenu("Chemistry marks: ")
                        mathGrade = intMenu("Mathematics marks: ")
                        econGrade = intMenu("Economics marks: ")
                        if 0<=phyGrade<=100 and 0<=chemGrade<=100 and 0<=mathGrade<=100 and 0<=econGrade<=100:
                            print("==================================\n"
                            f"Student Name: {student_name}\n"
                            f"Student ID: {studentID}\n"
                            f"Physics marks: {phyGrade}\n"
                            f"Chemistry marks: {chemGrade}\n"
                            f"Mathematics marks: {mathGrade}\n"
                            f"Economics marks: {econGrade}\n"
                            "==================================")
                            confirmation = input("Save the following data? (Y/N) ")
                            if confirmation.lower() == "y":
                                print("Student's data has been saved.")
                                student_data.append(
                                    {'name':student_name,'idNo':studentID,'phy':phyGrade,'chem':chemGrade,'math':mathGrade,'econ':econGrade}
                                ) # Adds new data to old data. This will be automatically sorted.
                                sortStudentData()
                            elif confirmation.lower() == "n":
                                print("Student's data is not saved to database.")
                                print("Returning to previous menu.")
                            else: 
                                print("Invalid input.")
                                print("Returning to previous menu.")
                        else: print("One of the inputted marks is invalid.")
                    else: print("Invalid student name.")
        elif new_menu == 2: break

def updateStudent(): # Update student data
    # Update has several functions so set some variables to global variables.
    global updateID
    global updateIndex
    while True:
        if len(student_data) == 0: # Checks if there are no data.
            print("No student data is available.")
            print("Please input at least one student data.")
            break
        else:
            print("==================================\n"
            "Update Student Menu:\n"
            "1. Update student data\n"
            "2. Back to Main Menu\n"
            "==================================")
            update_menu = intMenu("Input menu number: ")
            if update_menu == 1:
                updateID = intMenu("Input Student ID to update: ")
                while updateID not in student_id_list: # Checks if student ID exists.
                    print("Student ID is not found.")
                    print("Please input a valid student ID.")
                    updateID = intMenu("Input Student ID to update: ")
                else:
                    updateIndex = student_id_list.index(updateID)
                    allStudentsData(updateIndex,range(updateIndex,updateIndex+1))
                    print("==================================")
                    confirmation = input("Are you sure you want to modify this student's data? (Y/N) ")
                    if confirmation.lower() == "y":
                        updateInfo() # Second function to update
                    elif confirmation.lower() == "n":
                        print("Cancelled updating operation.")
                        print("Returning to previous menu.")
                    else: 
                        print("Invalid input.")
                        print("Returning to previous menu.")
            elif update_menu == 2: break
            
def updateInfo(): # Second function to update
    while True:
        print("==================================\n"
            "Please note that Student ID and student name cannot be modified.\n"
            "1. Physics Grade\n"
            "2. Chemistry Grade\n"
            "3. Mathematics Grade\n"
            "4. Economics Grade\n"
            "5. Back\n"
            "==================================")
        infoMenu = intMenu("Choose value to update: ")
        if 1 <= infoMenu <= 5:
            if infoMenu == 5: break
            else: 
                updateGrade(infoMenu) # Third function to update
                break
        else:
            print("Invalid input. Enter a valid menu number.")

def updateGrade(subject): # subject = infoMenu
    gradeInput = intMenu(f"Updated {subName[subject]} Grade: ")
    if 0 <= gradeInput <= 100:
        print("==================================\n"
              f"Student Name: {student_data[updateIndex]['name']}\n"
              f"Student ID: {student_data[updateIndex]['idNo']}\n"
              f"Old {subName[subject]} marks: {student_data[updateIndex][subNameShort[subject]]}\n"
              f"New {subName[subject]} marks: {gradeInput}\n"
              "==================================")
        confirmation2 = input("Update the student's data? (Y/N) ")
        if confirmation2.lower() == "y":
            print("Student's data has been updated.")
            student_data[updateIndex][subNameShort[subject]] = gradeInput
        elif confirmation2.lower() == "n":
            print("Student's data is not updated to the database.")
            print("Returning to the previous menu.")
        else:
            print("Invalid input.")
            print("Returning to the previous menu.")
    else:
        print("Invalid input.")

def delStudent(): # Delete student data
    while True:
        if len(student_data) == 0:
            print("No student data is available.")
            print("Please input at least one student data.")
            break
        else:
            print("==================================\n"
            "Remove Student Menu:\n"
            "1. Remove student data\n"
            "2. Back to Main Menu\n"
            "==================================")
            del_menu = intMenu("Input menu number: ")
            if del_menu == 1:
                delID = intMenu("Input Student ID to delete: ")
                while delID not in student_id_list:
                    print("Student ID is not found.")
                    print("Please input a valid student ID.")
                    delID = int(input("Input Student ID to delete: "))
                else:
                    delIndex = student_id_list.index(delID)
                    allStudentsData(delIndex,range(delIndex,delIndex+1))
                    print("==================================")
                    confirmation = input("Are you sure you want to remove this student's data? (Y/N) ")
                    if confirmation.lower() == "y":
                        student_data.pop(delIndex)
                        print("Student's data has been deleted.")
                        sortStudentData()
                    elif confirmation.lower() == "n":
                        print("Cancelled deleting operation.")
                        print("Returning to previous menu.")
                    else: 
                        print("Invalid input.")
                        print("Returning to previous menu.")
            elif del_menu == 2: break

def statsMenu(): # Statistics of inputted students
    while True:
        if len(student_data) == 0:
            print("No student data is available.")
            print("Please input at least one student data.")
            break
        else:
            print("==================================\n"
            "Students Statistics Menu:\n"
            "1. Pass rate\n"
            "2. Average marks\n"
            "3. Back to Main Menu\n"
            "==================================")
            stats_menu = intMenu("Input menu number: ")
            if stats_menu == 1: gradeStats(1) # Second part to statistics function
            elif stats_menu == 2: gradeStats(2)
            elif stats_menu == 3: break

def gradeStats(option):
    while True:
        print("==================================\n"
            "Select subject:\n"
            "1. Physics Grade\n"
            "2. Chemistry Grade\n"
            "3. Mathematics Grade\n"
            "4. Economics Grade\n"
            "5. Back\n"
            "==================================")
        infoMenu = intMenu("Choose subject to display: ")
        if 1 <= infoMenu <= 5:
            if infoMenu == 5: break
            else: 
                if option == 1:
                    statsCalc(infoMenu,"pass") # Third part to statistics functioon
                    break
                else:
                    statsCalc(infoMenu,"avg")
                    break
        else:
            print("Invalid input. Enter a valid menu number.")

def statsCalc(subject,func): # subject = infoMenu, func determines whether to show pass rate or average grades.
    passNum = 0
    total_grades = 0
    for i in range(len(student_data)):
        total_grades += student_data[i][subNameShort[subject]]
        if student_data[i][subNameShort[subject]] > passGrade:
           passNum += 1 # Number of students that passed
    pass_rate = round(( passNum / len(student_data) ) * 100,2)
    average = round(( total_grades / len(student_data)),1)
    if func == "pass":
        print(f"The pass rate for {subName[subject]} is {pass_rate}%.")
    elif func == "avg":
        print(f"The average grade for {subName[subject]} is {average}.")

def rankPoints():
    global rpIndex
    while True:
        if len(student_data) == 0:
            print("No student data is available.")
            print("Please input at least one student data.")
            break
        else:
            print("==================================\n"
            "Rank Points Calculation Menu:\n"
            "1. Student Rank Points\n"
            "2. Rank Point System\n"
            "3. Back to Main Menu\n"
            "==================================")
            rp_menu = intMenu("Input menu number: ")
        if rp_menu == 1:
            rpID = intMenu("Input Student ID: ")
            while rpID not in student_id_list:
                print("Student ID is not found.")
                print("Please input a valid student ID.")
                rpID = intMenu("Input a valid Student ID: ")
            else:
                rpIndex = student_id_list.index(rpID)
                allStudentsData(rpIndex,range(rpIndex,rpIndex+1))
                rpCount() # Second part in RP calculation function
        elif rp_menu == 2:
            print('''==================================
The rank point system are as follows:
Grade     | Rank Point (RP)
> 70      | 20
60 - 70   | 17.5
55 - 60   | 15
50 - 54   | 12.5
45 - 59   | 10
40 - 44   | 5
< 39      | 0
Your total RP will be summed and will be used to determine
whether you are eligible for university or not.
A minimum of 50 RP is required to be eligible for university.''')
        elif rp_menu == 3: break

def rpCount():
    rankPoint = 0
    for i in range(len(subNameShort)):
        mark = student_data[rpIndex][subNameShort[i+1]]
        for grade_range, rp in rank_points_data.items():
            # grade_range and rp is defined in the rank_points_data dictionary above
            if '-' in grade_range:
                lower_bound,upper_bound = map(int,grade_range.split('-')) # create the range for the marks
                if lower_bound <= mark <= upper_bound: # 60-69, 55-59, 50-54, 45-49, etc
                    rankPoint += rp
                    break
            else:
                if mark > int(grade_range): # for 70+
                    rankPoint += rp
                    break
    print(f"Your total Rank Points is: {rankPoint}.")
    if rankPoint < 50: print(f"You are ineligible for university.")
    else: print(f"You are eligible for university.")

while True: # Main Program
    main_menu()
    if menu == 0:
        print("Program Terminated.")
        break
    elif menu == 1:
        studentsList()
    elif menu == 2:
        newStudent()
    elif menu == 3:
        updateStudent()
    elif menu == 4:
        delStudent()
    elif menu == 5:
        statsMenu()
    elif menu == 6:
        rankPoints()
    else:
        print("Input invalid.")


