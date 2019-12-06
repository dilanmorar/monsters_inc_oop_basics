from Building_class import *

class Lecture_Theatres(Building):
    def __init__(self, location, lt_number):
        super(). __init__(location)
        self.lt_number = lt_number