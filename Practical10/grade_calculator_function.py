#calculate the total mark
def calculate(student_name, student_grade_for_the_code_portfolio, student_grade_for_the_poster_presentation, student_grade_in_the_final_exam):
    mark=student_grade_for_the_code_portfolio*0.4+student_grade_for_the_poster_presentation*0.3+student_grade_in_the_final_exam*0.3#calculate the total grade from four grades
    return student_name, mark #return student name and total grade

#example
print(calculate('a',80,70,80))
