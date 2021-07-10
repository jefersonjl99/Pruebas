plural_laminas = {'escudo': 'escudos', 'equipo': 'equipos',
                  'icono': 'iconos', 'estrella': 'estrellas', 'normal': 'normales'}


def tipos_lamina(laminas):
    tipos_laminas = []
    for i in laminas:
        if plural_laminas.get(i) not in tipos_laminas:
            tipos_laminas.append(plural_laminas.get(i))
    return tipos_laminas
    # "escudos", "equipos", "iconos", "estrellas", o “normales”.


def laminas_faltantes_tipo(laminasFaltantes, tiposLamina, tipoLamina):
    numeroLaminaFaltante = []
    for i in laminasFaltantes:
        if tiposLamina[i] == tipoLamina:
            numeroLaminaFaltante.append(i)
    return numeroLaminaFaltante


def me_faltan(listaAjena, miLista):
    listaCambios = []
    for i in listaAjena:
        if i not in miLista:
            listaCambios.append(i)
    return listaCambios


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
