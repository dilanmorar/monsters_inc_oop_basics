from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, colour, age,  skills, student_id, grade):
        super().__init__(name, colour, age,  skills)
        self.student_id = student_id
        self.grade = grade

student1 = Student_Monsters('Dave', '10 eyes', '1', 'pass')
print(student1.name)