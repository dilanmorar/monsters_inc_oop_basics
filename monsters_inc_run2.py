from Student_Monsters_class import *
from Lecture_Theatres_class import *
from Spooky_Workshops_class import *

while True:
    print('Choose option: ')
    print('1. create a monster')
    print('2. list all workshops')
    print('3. add students to workshops')
    print('4. see students grade')
    print('5. students full information')
    print('6. search for student by name')
    user_choice = input('Choose one of the options above: ')

    if user_choice == '1':
        print('Creating a monster:')
        users_monsters_name = input('What is your monsters name? ')
        users_monsters_skill = input('What is your monsters skill? ')
        users_monsters_grade = input('What is your monsters grade? ')
        users_monsters_student_id = input('What is your monsters students id? ')
        users_monster = Student_Monsters(users_monsters_name, users_monsters_skill, users_monsters_grade, users_monsters_student_id)
        print('Monster created')
        break

    elif user_choice == '2':
        print('List of running workshops: ')
        for subject in running_workshops:
            print(subject.scary_subject)
        break

    elif user_choice == '3':
        chosen_student = input('What student do you want to add to a workshop: ')
        chosen_workshop = input('What subject do you want your student to be added to: ')
        if chosen_workshop == 'Scare':
            workshop1.add_students(chosen_student)
        elif chosen_workshop == 'Strength':
            workshop2.add_students(chosen_student)
        elif chosen_workshop == 'Invisibility':
            workshop3.add_students(chosen_student)
        else:
            print('Subject does not exist')
            break
        break

    elif user_choice == '4':
        student_id = input("Student's name you want the grade of: ")
        for Student_Monsters in students:
            if student_id == Student_Monsters.student_id:
                print(Student_Monsters.grade)
        break

    elif user_choice == '5':
        student_id = input('What student do you want full information on: ')
        for Student_Monsters in students:
            if student_id == Student_Monsters.student_id:
                print(Student_Monsters.name)
                print(Student_Monsters.student_id)
                print(Student_Monsters.grade)

        break

    elif user_choice == '6':
        student_name = input('What is the name of the student you want to search for: ')
        for Student_Monsters in students:
            if student_name == Student_Monsters.name:
                print(Student_Monsters.student_id)
                print(Student_Monsters.skills)
                print(Student_Monsters.grade)
        break

    else:
        break