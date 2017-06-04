import math

a = input("Digita il numero: ")
b = input("Digita il numero: ")
c = input("Digita il numero: ")




radice = math.sqrt(b**2 - (4*a*c))
soluzione = (-b- radice)/2*a
soluzione1 = (-b + radice)/2*a

print "x1 = " + str(soluzione) + "\n" + "x2 = " + str(soluzione1)