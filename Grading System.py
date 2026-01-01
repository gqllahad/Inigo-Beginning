student_name = str
student_section = str
student_holder = {}


def student_info(name, section):
    student_holder[name] = section

def attendance(attendance_holder, attendance_grade, attendance_percentile):
    attendance_holder = ""
    attendance_grade = 0.0
    attendance_counter = 0
    attendance_record = int(input("Enter number of attendance record : "))
    if attendance_record < 1 or attendance_record > 3:
        print("Error!")
    else:
        attendance_date = 5
        for att in range(attendance_record):
            print(f"Date: 3/{attendance_date}/2024")
            attendance_remark = input("Remarks [present][absent] :  ")
            if attendance_remark == "present".lower():
                attendance_holder += (
                    "|3/{}/2024 : {} \t\t\t    |\t\t\t\t\t\t  |\t\t\t\t\t\t  |\n|\t\t\t".format(
                        attendance_date, attendance_remark))
                attendance_counter += 1
            elif attendance_remark == "absent".lower():
                attendance_holder += (
                    "|3/{}/2024 : {} \t\t\t    |\t\t\t\t\t\t  |\t\t\t\t\t\t  |\n|\t\t\t".format(
                        attendance_date, attendance_remark))
            else:
                print("Invalid!")
                break
            attendance_date += 5
    attendance_grade = round((attendance_counter * attendance_percentile), 2)
    print(round(attendance_grade, 2))
    return attendance_holder, attendance_grade


def class_standing(class_standing_grade, class_standing_percentile):
    class_quiz = int(input("Enter quiz score (0 - 100) ; "))
    if class_quiz < 0 or class_quiz > 100:
        print("Invalid number!")
    else:
        quiz_score = ((class_quiz / 100) * class_standing_percentile)

    class_activity = int(input("Enter activity score (0 - 100) : "))
    if class_activity < 0 or class_activity > 100:
        print("Invalid number!")
    else:
        activity_score = ((class_activity / 100) * class_standing_percentile)

    class_casestudy = int(input("Enter Case Study score (0 - 100) : "))
    if class_casestudy < 0 or class_casestudy > 100:
        print("Invalid number!")
    else:
        casestudy_score = ((class_casestudy / 100) * class_standing_percentile)

    class_standing_grade = round(quiz_score + activity_score + casestudy_score, 2)
    print(class_standing_grade)
    return class_standing_grade


def major_exam(major_exam_grade,major_exam_percentile):
    class_major = int(input("Enter Major exam score (0 - 100) : "))
    if class_major < 0 or class_major > 100:
        print("Invalid number!")
    else:
        major_exam_grade = round(((class_major / 100) * major_exam_percentile), 2)
    return major_exam_grade


def project_wow(project_holder, project_percentile):
    class_project_finals = int(input("Enter Project Score (0 - 100) ; "))
    if class_project_finals < 0 or class_project_finals > 100:
        print("Invalid number!")
    else:
        finals_project_grade = round(((class_project_finals / 100) * project_percentile), 2)
    return project_holder

def final_overall_grade(search_student,student_holder,prelim,midterm,semi_final,finals):
    final_grade = ((prelim + midterm + semi_final + finals) / 4)
    print(f""" Final Grade: 
                   Name: {search_student} Section: {student_holder[search_student]}

                   [x]Prelim  Grade : {prelim}
                   [x]MidTerm Grade : {midterm}
                   [x]Semi-Finals Grade : {semi_final}
                   [x]Finals Grade : {finals}
                   ______________________________________________________
                   Final Grade : {round(final_grade, 2)}
                """)

def main():
    # Grading variables
    attendance_percentile = (20 / 3)
    class_standing_percentile = (40 / 3)
    major_exam_percentile_terms = 40
    major_exam_project_percentile_finals = 20

    prelim_attendance_holder = ""
    prelim_attendance_grade = 0.00
    prelim_class_standing_grade = 0.00
    prelim_major_exam_grade = 0.00

    midterm_attendance_holder = ""
    midterm_attendance_grade = 0.00
    midterm_class_standing_grade = 0.00
    midterm_major_exam_grade = 0.00

    semi_finals_attendance_holder = ""
    semi_finals_attendance_grade = 0.00
    semi_finals_class_standing_grade = 0.00
    semi_finals_major_exam_grade = 0.00

    finals_attendance_holder = ""
    finals_attendance_grade = 0.00
    finals_class_standing_grade = 0.00
    finals_major_exam_grade = 0.00
    finals_project_grade = 0.00

    #Grade
    prelim_overall_grade = 0.00
    midterm_overall_grade = 0.00
    semi_finals_overall_grade = 0.00
    finals_overall_grade = 0.0
    final_grade = 0.0

    flag = True
    flag_3 = True
    for x in range(1):
        student_name = input("Enter student's full name : ")
        student_section = input("Enter student's section : ")
        student_info(student_name, student_section)

    while flag:
        search_a_student = input("Enter student's name you want to manage : ")
        search_student = student_holder.get(search_a_student)
        if search_student:
            flag = False
        else:
            first_option = input("\nDo you want to try again? [yes][no] : ").lower()
            if first_option == 'no':
                exit()
            elif first_option == 'yes':
                continue
            else:
                print("Name not found!\n")
                second_option = input("Still want to continue? [yes][no]").lower()
                if second_option == 'no':
                    exit()
                elif second_option == 'yes':
                    continue
                else:
                    print("Invalid choice! Please be more mature and read instructions!\n")
                    continue
    while flag_3:
     if search_a_student in student_holder:
        print("Name : ", search_a_student, "\nSection : ", student_holder[search_a_student])
        # Term_selection
        term_select = int(input("""
           Please select Term Grade :
           [1]Prelim
           [2]Midterm
           [3]Semi-Finals
           [4]Finals
           [5][Final Grade] 
           [5]Exit
           Choice : """))
        # Prelim
        if term_select == 1:
            grade_option_prelim = int(input("""
          Please select option you want:
          [1]Attendance
          [2]Class-Standing
          [3]Major Exam
          [4]Print Result
          [5]Back
          Choice : """))
            # Attendance (Prelim)
            if grade_option_prelim == 1:
                prelim_attendance_holder, prelim_attendance_grade = attendance(prelim_attendance_holder, prelim_attendance_grade, attendance_percentile)
                prelim_overall_grade += prelim_attendance_grade
                continue

            # Class Standing (Prelim)
            elif grade_option_prelim == 2:
                prelim_class_standing_grade = class_standing(prelim_class_standing_grade, class_standing_percentile)
                prelim_overall_grade += prelim_class_standing_grade
                continue

            # Major Exam (Prelim)
            elif grade_option_prelim == 3:
                prelim_major_exam_grade = major_exam(prelim_major_exam_grade, major_exam_percentile_terms)
                prelim_overall_grade += prelim_major_exam_grade
                continue


            # Print Result
            elif grade_option_prelim == 4:
                print("Prelim Grade : ", round(prelim_overall_grade, 2))
                print(f"""
===================================================================================================
|Prelim     | Attendance                        | Class Standing          | Major Exam            |
|           {prelim_attendance_holder}                                    |{prelim_class_standing_grade}                      |{prelim_major_exam_grade}                    |
|           |{prelim_attendance_grade}                                |                         |                       |
===================================================================================================
|MidTerm    | Attendance                        | Class Standing          | Major Exam            |
|           {midterm_attendance_holder}                                    |{midterm_class_standing_grade}                      |{midterm_major_exam_grade}                    |
|           |{midterm_attendance_grade}                                |                         |                       |
===================================================================================================
|Semi-      | Attendance                        | Class Standing          | Major Exam            |
|  Finals   {semi_finals_attendance_holder}                                    |{semi_finals_class_standing_grade}                      |{semi_finals_major_exam_grade}                    |
|           |{semi_finals_attendance_grade}                                |                         |                       |
===================================================================================================
|Finals     | Attendance                        | Class Standing          | Major Exam/Project    |                   
|           {finals_attendance_holder}                                    |{finals_class_standing_grade}                     |{finals_major_exam_grade}                   |
|           |{finals_attendance_grade}                               |                         |{finals_project_grade}                   |
===================================================================================================
""")
                continue


            elif grade_option_prelim == 5:
                continue

        # Midterm
        elif term_select == 2:
            grade_option_midterm = int(input("""
         Please select option you want:
         [1]Attendance
         [2]Class-Standing
         [3]Major Exam
         [4]Print Result
         [5]Back
         """))
            #Attendance(Midterm)
            if grade_option_midterm == 1:
                midterm_attendance_holder, midterm_attendance_grade = attendance(midterm_attendance_holder, midterm_attendance_grade, attendance_percentile)
                midterm_overall_grade += midterm_attendance_grade
                continue

            # Class Standing (Midterm)
            elif grade_option_midterm == 2:
                midterm_class_standing_grade = class_standing(midterm_class_standing_grade, class_standing_percentile)
                midterm_overall_grade += midterm_class_standing_grade
                continue

            # Major Exam (Midterm)
            elif grade_option_midterm == 3:
                midterm_major_exam_grade = major_exam(midterm_major_exam_grade, major_exam_percentile_terms)
                midterm_overall_grade += midterm_major_exam_grade
                continue

            # Print Result
            elif grade_option_midterm == 4:
                    print("Prelim Grade : ", round(midterm_overall_grade, 2))
                    print(f"""
===================================================================================================
|Prelim     | Attendance                        | Class Standing          | Major Exam            |
|           {prelim_attendance_holder}                                    |{prelim_class_standing_grade}                      |{prelim_major_exam_grade}                    |
|           |{prelim_attendance_grade}                                |                         |                       |
===================================================================================================
|MidTerm    | Attendance                        | Class Standing          | Major Exam            |
|           {midterm_attendance_holder}                                    |{midterm_class_standing_grade}                      |{midterm_major_exam_grade}                    |
|           |{midterm_attendance_grade}                                |                         |                       |
===================================================================================================
|Semi-      | Attendance                        | Class Standing          | Major Exam            |
|  Finals   {semi_finals_attendance_holder}                                    |{semi_finals_class_standing_grade}                      |{semi_finals_major_exam_grade}                    |
|           |{semi_finals_attendance_grade}                                |                         |                       |
===================================================================================================
|Finals     | Attendance                        | Class Standing          | Major Exam/Project    |                   
|           {finals_attendance_holder}                                    |{finals_class_standing_grade}                     |{finals_major_exam_grade}                   |
|           |{finals_attendance_grade}                               |                         |{finals_project_grade}                   |
===================================================================================================
""")
            continue


        # Semi-Finals
        elif term_select == 3:
            grade_option_semi_finals = int(input("""
         Please select option you want:
         [1]Attendance
         [2]Class-Standing
         [3]Major Exam
         [4]Print Result
         [5]Back
         """))
            # Attendance(Semi-Finals)
            if grade_option_semi_finals == 1:
                semi_finals_attendance_holder, semi_finals_attendance_grade = attendance(semi_finals_attendance_holder, semi_finals_attendance_grade, attendance_percentile)
                semi_finals_overall_grade += semi_finals_attendance_grade
                continue

            # Class Standing (Semi-Finals)
            elif grade_option_semi_finals == 2:
                semi_finals_class_standing_grade = class_standing(midterm_class_standing_grade, class_standing_percentile)
                semi_finals_overall_grade += semi_finals_class_standing_grade
                continue

            # Major Exam (Semi-finals)
            elif grade_option_semi_finals == 3:
                semi_finals_major_exam_grade = major_exam(semi_finals_major_exam_grade, major_exam_percentile_terms)
                semi_finals_overall_grade += semi_finals_major_exam_grade
                continue

             # Print Result
            elif grade_option_semi_finals == 4:
                    print("Semi-finals Grade : ", round(semi_finals_overall_grade, 2))
                    print(f"""                   
===================================================================================================
|Prelim     | Attendance                        | Class Standing          | Major Exam            |
|           {prelim_attendance_holder}                                    |{prelim_class_standing_grade}                      |{prelim_major_exam_grade}                    |
|           |{prelim_attendance_grade}                                |                         |                       |
===================================================================================================
|MidTerm    | Attendance                        | Class Standing          | Major Exam            |
|           {midterm_attendance_holder}                                    |{midterm_class_standing_grade}                      |{midterm_major_exam_grade}                    |
|           |{midterm_attendance_grade}                                |                         |                       |
===================================================================================================
|Semi-      | Attendance                        | Class Standing          | Major Exam            |
|  Finals   {semi_finals_attendance_holder}                                    |{semi_finals_class_standing_grade}                      |{semi_finals_major_exam_grade}                    |
|           |{semi_finals_attendance_grade}                                |                         |                       |
===================================================================================================
|Finals     | Attendance                        | Class Standing          | Major Exam/Project    |                   
|           {finals_attendance_holder}                                    |{finals_class_standing_grade}                     |{finals_major_exam_grade}                   |
|           |{finals_attendance_grade}                               |                         |{finals_project_grade}                   |
===================================================================================================
""")
                    continue

        # Finals
        elif term_select == 4:
            grade_option_finals = int(input("""
         Please select option you want:
         [1]Attendance
         [2]Class-Standing
         [3]Major Exam
         [4]Project
         [5]Print Result
         [6]Back
         """))
            # Attendance(Finals)
            if grade_option_finals == 1:
                finals_attendance_holder, finals_attendance_grade = attendance(finals_attendance_holder, finals_attendance_grade, attendance_percentile)
                finals_overall_grade += finals_attendance_grade
                continue

            # Class Standing (Finals)
            elif grade_option_finals == 2:
                finals_class_standing_grade = class_standing(finals_class_standing_grade, class_standing_percentile)
                finals_overall_grade += finals_class_standing_grade
                continue

            # Major Exam (finals)
            elif grade_option_finals == 3:
                finals_major_exam_grade = major_exam(finals_major_exam_grade, major_exam_project_percentile_finals)
                finals_overall_grade += finals_major_exam_grade
                continue

            # Project(Finals)
            elif grade_option_finals == 4:
                finals_project_grade = project_wow(finals_project_grade, major_exam_project_percentile_finals)
                finals_overall_grade += finals_project_grade
                continue

             # Print Result
            elif grade_option_finals == 5:
                    print("Finals Grade : ", round(finals_overall_grade, 2))
                    print(f"""                   
===================================================================================================
|Prelim     | Attendance                        | Class Standing          | Major Exam            |
|           {prelim_attendance_holder}                                    |{prelim_class_standing_grade}                      |{prelim_major_exam_grade}                    |
|           |{prelim_attendance_grade}                                |                         |                       |
===================================================================================================
|MidTerm    | Attendance                        | Class Standing          | Major Exam            |
|           {midterm_attendance_holder}                                    |{midterm_class_standing_grade}                      |{midterm_major_exam_grade}                    |
|           |{midterm_attendance_grade}                                |                         |                       |
===================================================================================================
|Semi-      | Attendance                        | Class Standing          | Major Exam            |
|  Finals   {semi_finals_attendance_holder}                                    |{semi_finals_class_standing_grade}                      |{semi_finals_major_exam_grade}                    |
|           |{semi_finals_attendance_grade}                                |                         |                       |
===================================================================================================
|Finals     | Attendance                        | Class Standing          | Major Exam/Project    |                   
|           {finals_attendance_holder}                                    |{finals_class_standing_grade}                     |{finals_major_exam_grade}                   |
|           |{finals_attendance_grade}                               |                         |{finals_project_grade}                   |
===================================================================================================
""")
                    continue
        #Final Grade!
        elif term_select == 5:
            final_overall_grade(search_a_student, student_holder[search_a_student], prelim_overall_grade, midterm_overall_grade, semi_finals_overall_grade, finals_overall_grade)
            continue

        # Exit
        elif term_select == 6:
            exit("GoodBye")
        else:
            print("Invalid option!")


    else:
        print("Name not found!")


main()
