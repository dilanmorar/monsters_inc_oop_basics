from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, skills,student_id, grade):
        super().__init__(name, skills)
        self.student_id = student_id
        self.grade = grade

student1 = Student_Monsters('Dave', ['freaky'], '1', 'pass')
student2 = Student_Monsters('Mike', 'intelligence', '2', 'pass')
student3 = Student_Monsters('Randall', 'invisible', '3', 'pass')
student4 = Student_Monsters('Sulley', 'v.scary', '4', 'pass')
student5 = Student_Monsters('Sock', 'stank', '5', 'pass')
student6 = Student_Monsters('Bully', 'aggression', '6', 'pass')

print(student1.skills)
student1.add_skills('stretchy arms')
print(student1.skills)


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
