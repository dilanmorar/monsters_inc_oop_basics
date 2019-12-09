from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, skills, student_id, grade):
        super().__init__(name, skills)
        self.student_id = student_id
        self.grade = grade

# print(student1.skills)
# student1.add_skills('stretchy arms')
# print(student1.skills)

# ex_student = Student_Monsters('Dave', ['freaky'], '1', 'pass')
#
# print('Should print student monster name: ')
# print(ex_student.name)
#
# print('Should print student monster skills: ')
# print(student1.skills)
#
# print('Should print student monster student id: ')
# print(student1.student_id)
#
# print('Should print student monster grade: ')
# print(student1.grade)

