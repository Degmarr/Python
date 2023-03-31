from hw1 import Human
from hw1 import Archon

class CatalistUser(Human, Archon):
    
    def Attack(self):
        print("attacks with a catalyst")

    def WhoAmI(self):
        print("I am a ", CatalistUser.Get_Element(self), " catalyst user")


    