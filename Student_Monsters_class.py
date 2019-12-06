from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, skills, colour, age, student_id, grade, course):
        super().__init__(name, skills, colour, age)
        self.student_id = student_id
        self.grade = grade
        self.course = course

student1 = Student_Monsters('Dave', '10 eyes', 'blue', '22', '1', 'pass', 'scare')
student2 = Student_Monsters('Mike', 'intelligence', 'green', '18', '2', 'pass', 'scare')
student3 = Student_Monsters('Randall', 'invisible', 'purple', '20', '3', 'pass', 'scare')

# print('Should print student monster name: ')
# print(student1.name)
#
# print('Should print student monster colour: ')
# print(student1.colour)
#
# print('Should print student monster age : ')
# print(student1.age)
#
# print('Should print student monster skills: ')
# print(student1.skills)
#
# print('Should print student monster student id: ')
# print(student1.student_id)
#
# print('Should print student monster grade: ')
# print(student1.grade)

# print('Should print student monster course: ')
# print(student1.course)