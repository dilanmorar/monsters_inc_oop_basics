from Student_Monsters_class import *
from Lecture_Theatres_class import *
from Spooky_Workshops_class import *

# creating 3 student monsters
student1 = Student_Monsters('Dave', ['freaky'], '1', 'pass')
student2 = Student_Monsters('Mike', 'intelligence', '2', 'pass')
student3 = Student_Monsters('Randall', 'invisible', '3', 'pass')

# students added to an empty list
students = []
print(students)
students.append(student1.name)
print(students)

# create 3 spooky workshops
workshop1 = Spooky_Workshops('Scare', 'Prof. Scary', 'Scary Building', [])
workshop2 = Spooky_Workshops('Strength', 'Prof. Strength', 'Strength Building', [])
workshop3 = Spooky_Workshops('Invisiblity', 'Prof. Invisibility', 'Invisibility Building', [])

# workshops added to list of running workshops
running_workshops = []
print(running_workshops)
running_workshops.append(workshop1.scary_subject)
print(running_workshops)

# show grade of student
print(student1.grade)

# adding student and print id
print(workshop1.list_students)
workshop1.add_students(student1.student_id)
print(workshop1.list_students)
