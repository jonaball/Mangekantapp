import math as m

# ------------ Hovedklasse ----------- #

class Mangekant:
    def __init__(self,navn:str, antall_sider:int, sidelengder:list):
        self.navn= navn
        self.antall_sider = antall_sider
        self.sidelengder = sidelengder
    def omkrets(self):
        return sum(self.sidelengder)
    def visinfo(self):
        return f'{self.navn} har {self.antall_sider} sider, sidene har lengdene {self.sidelengder} og omkretsen er {self.omkrets()}'

# Funksjoner for enklere bruk og definering av mangekanter
# Kanskje flytte disse inn i sine egne underklasser (eksempel: rekt_define() inn i Rektangel() klassen)?
# I stedet for å appende objektene til en liste, la oss skrive det i et document så det blir lagret. bruke open() og .write()
mangekanter = []
def rekt_define():
    rektangel = Mangekant("Rektangel",4,[int(x) for x in input("skriv inn sidelengdene til rektangelen (med en ',' i mellom): ").split(",")])
    mangekanter.append(rektangel)

def trek_define():
    trekant = Mangekant("Trekant",3,[int(x) for x in input(f"skriv inn sidelengdene til trekanten (med en ',' i mellom): ").split(",")])
    mangekanter.append(trekant)

def kvad_define():
    kvadrat = Mangekant("Kvadrat",4,[int(x) for x in input(f"skriv inn sidelengdene til kravdratet (med en ',' i mellom): ").split(",")])
    mangekanter.append(kvadrat)

# ----------- Underklasser ------------- #

class Rektangel(Mangekant):
    def __init__(self, navn, lengde, bredde):
        super.__init__(navn)
        self.lengde = lengde
        self.bredde = bredde

    def arealrektangel(self):
        return self.lengde * self.bredde
    
class Kvadrat(Rektangel):
    def __init__(self, navn, lengde, ):
        super().__init__(navn, lengde,)
    def arealkvadrat(self):
        return self.lengde * self.lengde

class Trekant(Mangekant):
    def __init__(self, navn: str, antall_sider: int, sidelengder: list):
        super().__init__(navn, antall_sider, sidelengder)
    def arealtrekant(self):
        s = self.omkrets() * 0.5  
        return round(m.sqrt(s * (s - self.sidelengder[0]) * (s - self.sidelengder[1]) * (s - self.sidelengder[2])),1)
    def vistrekant(self):
        return f'{self.navn}: Sidelengder: {self.sidelengder}, Areal:{self.arealtrekant()}'

# Trenger vi disse?

#  |
#  |
#  V

# trekant_liste = []
# trekant1 = Trekant("Trekant 1",3,[4,4.2,5])
# trekant2 = Trekant("Trekant 2",3,[5,5.6,5.6])
# trekant3 = Trekant("Trekant 3",3,[4,4,4])
# trekant4 = Trekant("Trekant 4",3,[4,6,7])
# trekant5 = Trekant("Trekant 5",3,[3,6.2,6.2])

# trekant_liste.append(trekant1)
# trekant_liste.append(trekant2)
# trekant_liste.append(trekant3)
# trekant_liste.append(trekant4)
# trekant_liste.append(trekant5)

# for ting in trekant_liste:
#     print(ting.vistrekant())
