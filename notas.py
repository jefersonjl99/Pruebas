
nota_juan=int(input("Ingrese la nota de Juan: "))
nota_pedro=2*nota_juan+4
nota_camila=(nota_juan+nota_pedro)//5

print(nota_juan,nota_pedro,nota_camila)

if nota_camila>0 and nota_camila<=20:
    print("uno")
elif nota_camila>20 and nota_camila<=30:
    print("dos")
elif nota_camila>30 and nota_camila<=50:
    print("tres")
else:
    print("cuatro")