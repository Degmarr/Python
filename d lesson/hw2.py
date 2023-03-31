from hw1 import Human

class ClaymoreUser(Human):

    def Attack(self):
        return print("attacks with a claymore")
    
    def WhoAmI(self):
        return print("I am a ", ClaymoreUser.Get_Element(self), " claymore user")

