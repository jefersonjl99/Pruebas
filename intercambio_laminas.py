plural_laminas = {'escudo': 'escudos', 'equipo': 'equipos',
                  'icono': 'iconos', 'estrella': 'estrellas', 'normal': 'normales'}


def tipos_lamina(laminas):
    tipos_laminas = []
    for i in laminas:
        if i in plural_laminas:
            if plural_laminas.get(i) not in tipos_laminas:
                tipos_laminas.append(plural_laminas.get(i))
        elif i not in tipos_laminas:
            tipos_laminas.append(i)
    return tipos_laminas


prueba = ['escudo', 'escudo', 'equipo', 'normal', 'normal',
          'estrella', 'icono', 'normal', 'normal', 'equipo']
print(tipos_lamina(prueba))


def laminas_faltantes_tipo(laminasFaltantes, tiposLamina, tipoLamina):
    numeroLaminaFaltante = []
    for i in laminasFaltantes:
        if tiposLamina[i] == tipoLamina:
            numeroLaminaFaltante.append(i)
    return numeroLaminaFaltante


prueba = [1, 3, 6, 8]
prueba0 = ['escudo', 'escudo', 'equipo', 'normal', 'normal',
           'estrella', 'icono', 'normal', 'normal', 'equipo']
prueba1 = 'normal'
print(laminas_faltantes_tipo(prueba, prueba0, prueba1))


prueba = [1, 3, 6, 8]
prueba0 = ['escudo', 'escudo', 'equipo', 'normal', 'normal',
           'estrella', 'icono', 'normal', 'normal', 'equipo']
prueba1 = 'escudo'
print(laminas_faltantes_tipo(prueba, prueba0, prueba1))


def me_faltan(listaAjena, miLista):
    listaCambios = []
    for i in listaAjena:
        if i not in miLista:
            listaCambios.append(i)
    return listaCambios


prueba = [3, 5, 7, 10, 15, 16]
prueba1 = [4, 10, 5, 8]
print(me_faltan(prueba, prueba1))


def cambiar(listaAjena, miLista):
    numeroCambiosAjenos = 0
    numeroCambiosMios = 0
    for i in listaAjena:
        if i not in miLista:
            numeroCambiosMios += 1

    for i in miLista:
        if i not in listaAjena:
            numeroCambiosAjenos += 1

    if numeroCambiosAjenos < numeroCambiosMios:
        r = numeroCambiosAjenos
    else:
        r = numeroCambiosMios
    return r


prueba = [3, 5, 7, 10, 15, 16]
prueba1 = [4, 10, 5, 8]
print(cambiar(prueba, prueba1))
