from Student_Monsters_class import *
from Lecture_Theatres_class import *
from Spooky_Workshops_class import *

student1 = Student_Monsters('Dave', ['freaky'], '1', 'pass')
student2 = Student_Monsters('Mike', 'intelligence', '2', 'pass')
student3 = Student_Monsters('Randall', 'invisible', '3', 'pass')

print(student1.skills)
student1.add_skills('stretchy arms')
print(student1.skills)
