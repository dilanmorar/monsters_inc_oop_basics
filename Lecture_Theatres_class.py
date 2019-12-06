from Building_class import *

class Lecture_Theatres(Building):
    def __init__(self, location, lt_name):
        super(). __init__(location)
        self.lt_name = lt_name


# lt1 = Lecture_Theatres('front', 'lt1', '100', )
# print('Should print location of lecture theatre: ')
# print(lt1.location)
# print('Should print name of lecture theatre: ')
# print(lt1.lt_name)

