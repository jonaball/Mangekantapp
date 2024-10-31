# dette er hvor en bruker kan lage mangekanter, og bruke funksjoner fra klassene for å regne med man
import inquirer as inq
import math

spørsmål = [

    # spørsmål[0]
    inq.List('figur',
            message="Hvilken type mangekant velger du?",
            choices=['Trekant', 'Firkant', 'Femkant', 'Sekskant'],
        ), 

    # spørsmål[1]
    inq.List('operasjon',
             message="Hva slags operasjon vil du gjøre med mangekanten?",
             choices=['Regne areal', 'annet'],
        ),
 ]

svar = inq.prompt(spørsmål)

if svar['figur'] == 'Trekant':
    # her går programmet videre hvis bruker har valgt trekant
    print("test")

if svar['figur'] == 'Firkant':
    # her går programmet videre hvis bruker har valgt firkant
    print()

if svar['figur'] == 'Femkant':
    # her går programmet videre hvis bruker har valgt femkant
    print()

if svar['figur'] == 'Sekskant':
    # her går programmet videre hvis bruker har valgt sekskant
    print()