from Building_class import *

class Lecture_Theatres(Building):
    def __init__(self, location, lt_name, capacity, floors = 1, rooms = 1):
        super(). __init__(location, floors, rooms)
        self.floors = floors
        self.rooms = rooms
        self.lt_name = lt_name
        self.capacity = capacity

lt1 = Lecture_Theatres('front', 'lt1', '100', )
print('Should print location of lecture theatre: ')
print(lt1.location)
print('Should print name of lecture theatre: ')
print(lt1.lt_name)
print('Should print capacity of lecture theatre: ')
print(lt1.capacity)
print('Should print floors in lecture theatre: ')
print(lt1.floors)
print('Should print rooms in lecture theatre: ')
print(lt1.rooms)
