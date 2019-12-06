from Monster_class import *

class Student_Monsters(Monster):
    def __init__(self, name, skills, colour, age, student_id, grade, course):
        super().__init__(name, skills, colour, age)
        self.student_id = student_id
        self.grade = grade
        self.course = course

    def add_skills(self, skill):
        chosen_monster = self
        chosen_monster.skills.append(skill)

student_dict = {'student1' : "Student_Monsters('Dave', 'freaky', 'blue', '22', '1', 'pass', 'scare')",
                'student2' : "Student_Monsters('Mike', 'intelligence', 'green', '18', '2', 'pass', 'scare')",
                'student3' : "Student_Monsters('Randall', 'invisible', 'purple', '20', '3', 'pass', 'scare')",
                'student4' : "Student_Monsters('Sulley', 'v.scary', 'purple and blue', '25', '4', 'pass', 'paranoia')",
                'student5' : "Student_Monsters('Sock', 'stank', 'orange and yellow', '20', '5', 'pass', 'paranoia')",
                'student6' : "Student_Monsters('Bully', 'agression', 'purple and green', '23', '6', 'pass', 'paranoia')",
}

print(student_dict.values(student1))

# print(student1.skills)
# student1.add_skills('stretchy arms')
# print(student1.skills)


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
