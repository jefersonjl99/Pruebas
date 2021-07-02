import json

tDisponibles = input()
tBuscadas = input()
precioSalida=0
tSalida=''

tBuscadas=tBuscadas.replace(" ", "")
data= json.loads(tDisponibles)

for i in tBuscadas:
    if(i in data):
        precioSalida+=data[i]
        tSalida+=i+' '

print(str(precioSalida)+"\n"+tSalida)