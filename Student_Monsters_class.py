from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, skills):
        super().__init__(Student_Monsters, student_id, grade)
        self.student_id = student_id
        self.grade = grade

student1 = Student_Monsters('Dave', '10 eyes')
print(student1.student_id)