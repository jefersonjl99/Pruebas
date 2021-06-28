producto=input()
pcu=int(input())
pvp=int(input())
cd=int(input())
ganancia=(pvp-pcu)*cd

print("Producto: {}\nCU: ${}\nPVP: ${}\nUnidades Disponibles: {}\nGanancia: ${}".format(producto,pcu,pvp,cd,ganancia))