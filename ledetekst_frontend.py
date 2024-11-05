# dette er hvor en bruker kan lage mangekanter, og bruke funksjoner fra klassene for å regne med man
import inquirer as inq
import Klasser_og_funksjoner.Funksjoner_for_mangekanter as f
import Klasser_og_funksjoner.Mangekant as m

# ------------ Spørsmål ------------ #

spørsmål1 = inq.List('figur',
            message="Hvilken type mangekant velger du?",
            choices=['Trekant', 'Rektangel', 'Kvadrat'],
        ),
mangekant_select = "" #holder track over hvilken type mangekant som er valgt

spørsmål2 = inq.List('operasjon',
            message="Hva slags operasjon vil du gjøre med mangekanten?",
            choices=['Regne Areal', 'Regne Omkrets', "Lagre en Mangekant"],
        ),

spørsmål3 = inq.List('trekant', 
            message="Har du alle sidelengdene til trekanten?",
            choices=['Ja', 'Nei']
        ),

# ------------ Svar-alternativer ----------- #

# -- Spørmsål 1
svar1 = inq.prompt(spørsmål1)
if svar1['figur'] == 'Trekant':
    mangekant_select = "trekant"
if svar1['figur'] == 'Rektangel':
    mangekant_select = "rektangel"
if svar1['figur'] == 'Kvadrat':
    mangekant_select = "kvadrat"

# -- Spørsmål 2
svar2 = inq.prompt(spørsmål2)
if svar2['operasjon'] == "Regne Areal":
    if mangekant_select == "trekant":
        # -- Spørmsål 3
        svar3 = inq.prompt(spørsmål3)
        if svar3['trekant'] == 'Ja':
            side_liste=[]
            side1 = int(input("Lengden til side 1: "))
            side2 = int(input("Lengden til side 2: "))
            side3 = int(input("Lengden til side 3: "))
            side_liste.append(side1)
            side_liste.append(side2)
            side_liste.append(side3)
            print(m.Trekant.arealtrekant(side_liste))
        if svar3['trekant'] == 'Nei':
            g = int(input("Grunnlinje: "))
            h = int(input("Høyde: "))
            print(f.arealTrekant(g,h))

    if mangekant_select == "rektangel":

        b = int(input("Bredde: "))
        h = int(input("Høyde: "))
        print(f.arealRektangel(b, h))
    if mangekant_select == "kvadrat":
        side = int(input("Sidelengde: "))
        print(f.arealKvadrat(side))
if svar2['operasjon'] == "Regne Omkrets":
    print("Ikke implementert")
if svar2['operasjon'] == "Lagre en Mangekant":
    if mangekant_select =="trekant":
        m.trek_define()
    if mangekant_select =="rektangel":
        m.rekt_define()
    if mangekant_select == "kvadrat":
        m.kvad_define()