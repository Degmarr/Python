from hw1 import Human
from hw1 import Archon
from hw2 import ClaymoreUser
from hw3 import Sworsdman
from hw4 import CatalistUser
 
Katheryne = Human("Snezhnevna", "Katheryna")
Katheryne.Set_Age(20)

Venti = Archon("Barbatos")
Venti.Set_Element("anemo")
Venti.SetAge(2671)

Zhongli = Archon("Morax")
Zhongli.Set_Element("Geo")
Zhongli.SetAge(6394)

Diluc = ClaymoreUser("Ragnvidr", "Diluc")    
Diluc.Set_Age(22)
Diluc.Set_Element("pyro")

Eula = ClaymoreUser("Lawrence", "Eula")
Eula.Set_Age(23)
Eula.Set_Element("cryo") 

Ayaka = Sworsdman("Kamisato", "Ayaka")
Ayaka.Set_Age(17)
Ayaka.Set_Element("cryo")

Kazuha = Sworsdman("Kaedehara", "Kazuha")
Kazuha.Set_Age(18)
Kazuha.Set_Element("anemo") 

Scara = CatalistUser("Kunikuzushi", "Scaramouche")     
Scara.SetAge(452)
Scara.Set_Element("electro")

LaSignora = CatalistUser("Lohefalter", "Rosalyne-Kruchka")
LaSignora.SetAge(526)
LaSignora.Set_Element("cryo")

print(" ")
print("Write a number, corresponding to the chosen answer")
print(" ")

c = int(input("Choose a character: Diluc(1), Eula(2), Ayaka(3), Kazuha(4),  Scaramouche(5), La Signora(6), Zhongli(7(), Venti(8), Katheryne(9) "))
print("")
print("Enter 0 to end")
print("")
a = 1
while a != 0:
    if c == 1:
        print("Hello. My name is ", Diluc.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", sep = "\n")
        a = int(input())
        if a == 1:
            print("My full name is ", Diluc.Get_name(), Diluc.Get_surname(), end = "\n")
        if a == 2:    
            print(Diluc.WhoAmI(), end = "\n")
        if a == 3:    
            print("I am", Diluc.Get_Age(), "years old", end = "\n")
        if a == 4:    
            print("My catchprase is ", Diluc.Talk("'We should prepare while we can, then make a preemtive strike against the enemy'"), end = "\n")
        if a == 5:    
            print("My idle action is ", Diluc.Idle("catching my owl"), end = "\n")
        if a == 6:
            print(Diluc.Get_name(), Diluc.Attack(), end = "\n")    
    elif c == 2:
        print("Hello. My name is ", Eula.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Eula.WhoAmI(), end = "\n")
        if a == 2:
            print("My full name is ", Eula.Get_name(), Eula.Get_surname(), end = "\n")
        if a == 3:
            print("I am", Eula.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Eula.Talk("'Aristocratic etiquette is all just for show.. just smile and nod along! I was forced to learn all the rules my heart, but even I don't tke them that seriosly'"), end = "\n")   
        if a == 5:
            print("My idle action is ", Eula.Idle("creating a big snowflake"), end = "\n")
        if a == 6:
            print(Eula.Get_name(), Eula.Attack(), end = "\n")    
    elif c == 3:
        print("Hello. My name is ", Ayaka.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Ayaka.WhoAmI(), end = "\n")
        if a == 2:
            print("My full name is ", Ayaka.Get_name(), Ayaka.Get_surname(), end = "\n")
        if a == 3:
            print("I am", Ayaka.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Ayaka.Talk("'a blade is like a tea-leaf. Only those who sample it many times can appreciate its true qualities'"), end = "\n")  
        if a == 5:
            print("My idle action is ", Ayaka.Idle("touching my sword and explaining its assignment"), end = "\n")
        if a == 6:
            print(Ayaka.Get_name(), Ayaka.Attack(), end = "\n")    
    if c == 4:
        print("Hello. My name is ", Kazuha.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Kazuha.WhoAmI(), end = "\n")
        if a == 2:
            print("My full name is ", Kazuha.Get_name(), Kazuha.Get_surname(), end = "\n")
        if a == 3:
            print("I am", Kazuha.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Kazuha.Talk("'Whenever in this this world i roam, I carry memory of my home.. This blade.. It is the last thing I have to the land of my birth'"), end = "\n")   
        if a == 5:
            print("My idle action is ", Kazuha.Idle("catching a leaf and making music on it"), end = "\n") 
        if a == 6:
            print(Kazuha.Get_name(), Kazuha.Attack(), end = "\n")    
    if c == 5:
        print("Hello. My name is ", Scara.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", "Changing landscape(7)", sep = "\n", end = "\n")
        a = int(input())
        if a == 1:
            print(Scara.WhoAmI(), end = "\n")
        if a == 2:
            print("My full name is ", Scara.Get_name(), Scara.Get_surname(), end = "\n")
        if a == 3:
            print("I am", Scara.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Scara.Talk("'There's no such thing as pure freedom in this world. Even the wind cannot blow on forever'"), end = "\n")
        if a == 5:
            print("My idle action is ", Scara.Idle("moking threatening  by an anemo elemental sphere"), end = "\n")
        if a == 6:
            print(Scara.Get_name(), Scara.Attack(), end = "\n")    
        if a == 7:
            print(Scara.Get_name(), Scara.Landscape("cut mountains by a lighning"), end = "\n")    
    if c == 6:
        print("Hello. My name is ", LaSignora.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", "Changing landscape(7)", sep = "\n")
        a = int(input())
        if a == 1:
            print(LaSignora.WhoAmI(), end = "\n")
        if a == 2:
            print("My full name is ", LaSignora.Get_name(), LaSignora.Get_surname(), end = "\n")
        if a == 3:
            print("I am", LaSignora.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", LaSignora.Talk("'Haha, you're trembling.. is it the cold, or just cowardice?'"), end = "\n")  
        if a == 5:
            print("My idle action is ", LaSignora.Idle("standing while my catalyst is levitating near me"), end = "\n")
        if a == 6:
            print(LaSignora.Get_name(), LaSignora.Attack(), end = "\n")    
        if a == 7:
            print(LaSignora.Get_name(), LaSignora.Landscape("froze the river"), end = "\n")    
    if c == 7:
        print("Hello. My name is ", Zhongli.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My real name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", "Changing landscape(7)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Zhongli.WhoAmI(), end = "\n")
        if a == 2:
            print("My real name is ", Zhongli.Get_name(), end = "\n")
        if a == 3:
            print("I am", Zhongli.GetAge(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Zhongli.Talk("'I will have order'"), end = "\n")
        if a == 5:
            print("My idle action is ", Zhongli.Idle("thoughtfully standinf and potating a mini comet around myself"), end = "\n")
        if a == 6:
            print(Zhongli.Get_name(), Zhongli.AttackS(), end = "\n")    
        if a == 7:
           print(Zhongli.Get_name(), Zhongli.Landscape("created a petrified mountain by  myriad of  polearms"), end = "\n")    
    if c == 8:
        print("Hello. My name is ", Venti.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My real name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", "Changing landscape(7)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Venti.WhoAmI(), end = "\n")
        if a == 2:    
            print("My real name is ", Venti.Get_name(), end = "\n")
        if a == 3:
            print("I am", Venti.GetAge(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Venti.Talk("'May the wind protect you'"), end = "\n")     
        if a == 5:
            print("My idle action is ", Venti.Idle("levitating and creating an anemo elemental sphere"), end = "\n")  
        if a == 6:
            print(Venti.Get_name(), Venti.Landscape("cut mountains by the wind"), end = "\n")       
    if c == 9:
        print("Hello. My name is ", Katheryne.Get_name(), ", what do you want to know about me?", end = "\n")
        print("My full name(1)", "Who i am(2)", "My age(3)", "My catchphrase(4)", "Me while standing(5)", "Attaking an enemy(6)", sep = "\n")
        a = int(input())
        if a == 1:
            print(Katheryne.WhoAmI(), end = "\n")
        if a == 2: 
            print("My full name is ", Katheryne.Get_name(), Katheryne.Get_surname(), end = "\n") 
        if a == 3:
            print("I am", Katheryne.Get_Age(), "years old", end = "\n")
        if a == 4:
            print("My catchprase is ", Katheryne.Talk("'Ad astra abyssoque! Welcime to the Adventures's Guild'"), end = "\n")     
        if a == 5:
            print("My idle action is ", Katheryne.Idle("just standing"), end = "\n")    
        if a == 6:
           print(Katheryne.Get_name(), Katheryne.Attack(), end = "\n")     


print("Goodbye, have a nice day <3")
