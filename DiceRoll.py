import random

class Die():
    def __init__(self, faces):
        self._faces = faces 

    def get_faces(self):
        return self._faces

#create die roll
    def roll_die(self):
        return random.randint(1,self._faces)
