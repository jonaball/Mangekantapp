# dette er hvor en bruker kan lage mangekanter, og bruke funksjoner fra klassene for å regne med man
import inquirer as inq
import Funksjoner_for_mangekanter
import Mangekant

spørsmål1 = inq.List('figur',
            message="Hvilken type mangekant velger du?",
            choices=['Trekant', 'Firkant', 'Femkant', 'Sekskant'],
        ), 

spørsmål2 = inq.List('operasjon',
             message="Hva slags operasjon vil du gjøre med mangekanten?",
             choices=['Regne Areal', 'Regne Omkrets', "Lagre en Mangekant"],
        ),

mangekant_select = "" #holder track over hvilken type mangekant som er valgt

svar1 = inq.prompt(spørsmål1)
if svar1['figur'] == 'Trekant':
    mangekant_select = "trekant"

if svar1['figur'] == 'Firkant':
    mangekant_select = "firkant"

if svar1['figur'] == 'Femkant':
    mangekant_select = "femkant"

if svar1['figur'] == 'Sekskant':
    mangekant_select = "sekskant"

svar2 = inq.prompt(spørsmål2)
if svar2 == "Regne Areal":
    