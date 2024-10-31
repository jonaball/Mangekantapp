# Arealet av trekant
def arealTrekant(grunnlinje, hoyde):
    return grunnlinje * hoyde * 0.5

arealT = arealTrekant(5, 10)

print(f"Arealet av trekanten er {arealT}")


# Arealet av kvadrat
def arealKvadrat(side):
    return side^2

arealK = arealKvadrat(5)

print(f"Arealet av kvadraten er {arealK}")


# Areal av Rektangel
def arealRektangel(grunnlinje, hoyde):
    return grunnlinje * hoyde

arealR = arealRektangel(5, 10)

print(f"Arealet av rektangelen er {arealR}")