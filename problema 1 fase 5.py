#HAROLD HOYOS
#FUNDAMENTOS DE PROGRAMACION





# Función para clasificar el compromiso de la sesión
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


# Matriz con la información de las sesiones
sesiones = [
    ["H1", 221, 9],
    ["H2", 40, 2],
    ["H3", 150, 7],
    ["H4", 60, 2],
    ["H5", 325, 18]
]

# Informe de clasificación
print("INFORME DE COMPROMISO DE SESIONES")
print("---------------------------------")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print("Cliente:", id_cliente)
    print("Clasificación:", clasificacion)
    print("---------------------------------")
