from Student_Monsters_class import *

class Spooky_Workshops():
    def __init__(self, course, staff, location, duration, student = []):
        self.scary_course = course
        self.staff = staff
        self.list_student_monsters = student
        self.location = location
        self.duration = duration

    def add_student(self, name):
        student_name = self
        student_name.list_student_monsters.append(name)

Scare_Workshop = Spooky_Workshops('scare', 'ghost', 'front', '2 years', students)
print('Should print list of students on the course "Scare": ')
if Scare_Workshop.scary_course == Student_Monsters.course:
    print(students.name)

# lists student monsters
# Scare_Workshop = Spooky_Workshops('paranoia', 'ghost', 'front', '2 years', students)
# print('Should print list of students on the course "paranoia": ')
# print(Scare_Workshop.list_student_monsters)