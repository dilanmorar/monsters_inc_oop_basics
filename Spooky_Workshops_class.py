from Student_Monsters_class import *

class Spooky_Workshops():
    def __init__(self, subject, staff, location, student_list):
        self.scary_subject = subject
        self.staff = staff
        self.list_students = student_list
        self.location = location

    def add_students(self, student):
        student_name = self
        student_name.list_students.append(student)

# scary_workshop = Spooky_Workshops('scary', 'none', 'front', [])
#
# print(scary_workshop.list_student_monsters)
# scary_workshop.add_students('Dave')
# print(scary_workshop.list_student_monsters)

# lists student monsters
# Scare_Workshop = Spooky_Workshops('paranoia', 'ghost', 'front', '2 years', students)
# print('Should print list of students on the course "paranoia": ')
# print(Scare_Workshop.list_student_monsters)