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
students.append(student1)
students.append(student2)
students.append(student3)
# students.extend(student1, student2, student3)
print(students)

# create 3 spooky workshops
workshop1 = Spooky_Workshops('Scare', 'Prof. Scary', 'Scary Building', [])
workshop2 = Spooky_Workshops('Strength', 'Prof. Strength', 'Strength Building', [])
workshop3 = Spooky_Workshops('Invisiblity', 'Prof. Invisibility', 'Invisibility Building', [])

# workshops added to list of running workshops
running_workshops = []
print(running_workshops)
running_workshops.append(student1)
running_workshops.append(student2)
running_workshops.append(student3)
# running_workshops.extend(workshop1, workshop2, workshop3)
print(running_workshops)

# iterate over the list of workshops and print
# number_of_running_workshops = len(running_workshops)
# count = 0
# while count<=number_of_running_workshops:
#     print((running_workshops[count].location))
#     count+=1
#
for subject in running_workshops:
    print(subject)

# iterate over the student list
# number_of_students = len(students)
# count = 0
# while count<=number_of_students:
#     print((student[count]))
#     count+=1

for student in students:
    print(student)


# show grade of student
print(student1.grade)

# adding student and print id
print(workshop1.list_students)
workshop1.add_students(student1.student_id)
print(workshop1.list_students)
