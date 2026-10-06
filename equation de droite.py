from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    print("Ce n'est pas une équation du second degrés")
else:
    delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b - sqrt(delta)) / (2*a)
    x2 = (-b + sqrt(delta)) / (2*a)
    print("Deux solutions :", x1, "et", x2)
elif delta == 0:
    x0 = -b / (2*a)
    print("Une solution double :", x0)
else:
    print("Aucune solution réelle")