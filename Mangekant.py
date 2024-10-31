class Mangekant:
    def __init__(self,navn:str, antall_sider:int, sidelengder:list):
        self.navn= navn
        self.antall_sider = antall_sider
        self.sidelengder = sidelengder
    def omkrets(self):
        return sum(self.sidelengder)
    def visinfo(self):
        return f'{self.navn} har {self.antall_sider} sider, sidene har lengdene {self.sidelengder} og omkretsen er {self.omkrets()}'


rektangel = Mangekant("Rektangel",4,[int(x) for x in input("skriv inn sidelengdene til rektangelen (med en ',' i mellom): ").split(",")])
trekant = Mangekant("Trekant",3,[int(x) for x in input(f"skriv inn sidelengdene til trekanten (med en ',' i mellom): ").split(",")])
kvadrat = Mangekant("Kvadrat",4,[int(x) for x in input(f"skriv inn sidelengdene til kravdratet (med en ',' i mellom): ").split(",")])

liste=[]
liste.append(rektangel)
liste.append(trekant)
liste.append(kvadrat)

for ting in liste:
    print(ting.visinfo())
