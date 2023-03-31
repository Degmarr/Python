class Human():
    __age1 = 0
    
    __element = "no element"

    def Attack(self):
        print("attacks")

    def __init__(self, surname, name):
        self.__surname = surname
        self.__name = name

    def Talk(self, message):
        return message

    def Idle(self, animation):
        return animation
    
    def Get_Age(self):
        return self.__age

    def Get_surname(self):
        return self.__surname

    def Get_name(self):
        return self.__name

    def Set_Age(self, age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self.__age = age

    def Set_surname(self,surname):
        self.__surname = surname

    def Set_name(self,name):
        self.__name = name

    def Get_Element(self):
        return self.__element

    def Set_Element(self, element):
        self.__element = element

    def WhoAmI(self):
        print("I am a human")
    

class Archon():
    __age2  = 0
    __element = "no element"

    def  AttackS(self):
        print("attacks powerfully")

    def __init__(self, name):
        self.__name = name

    def Landscape(self, landscape):
        return landscape

    def Talk(self, message):
        return message

    def Idle(self, animation):
        return animation
    
    def GetAge(self):
        return self.__age

    def Get_name(self):
        return self.__name

    def SetAge(self, age):
        if age < 0:
            print("Age cannot be negative")
        else:
            self.__age = age

    def Get_Element(self):
        return self.__element

    def Set_Element(self, element):
        self.__element = element

    def WhoAmI(self):
        print("I am a ", Archon.Get_Element(),  " archon")        

    def Set_name(self,name):
        self.__name = name



