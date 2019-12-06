from Building_class import *

class Lecture_Theatres(Building):
    def __init__(self, location, floors, rooms, lt_number, capacity):
        super(). __init__(location, floors, rooms)
        self.lt_number = lt_number
        self.capacity = capacity