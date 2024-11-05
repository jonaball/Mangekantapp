class Mangekant:
    def __init__(self,navn:str, antall_sider:int, sidelengder:list):
        self.navn= navn
        self.antall_sider = antall_sider
        self.sidelengder = sidelengder
    def omkrets(self):
        return sum(self.sidelengder)
    def visinfo(self):
        return f'{self.navn} har {self.antall_sider} sider, sidene har lengdene {self.sidelengder} og omkretsen er {self.omkrets()}'






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

import math as m

class Trekant(Mangekant):
    def __init__(self, navn: str, antall_sider: int, sidelengder: list):
        super().__init__(navn, antall_sider, sidelengder)
    def arealtrekant(self):
        s = self.omkrets() * 0.5  
        return round(m.sqrt(s * (s - self.sidelengder[0]) * (s - self.sidelengder[1]) * (s - self.sidelengder[2])),1)
    def vistrekant(self):
        return f'{self.navn}: Sidelengder: {self.sidelengder}, Areal:{self.arealtrekant()}'

