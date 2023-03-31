from hw1 import Human

class Sworsdman(Human):

    def Attack(self):
        print("attacks with a sword")

    def WhoAmI(self):
        print("I am a ", Sworsdman.Get_Element(self), " swordsman")


