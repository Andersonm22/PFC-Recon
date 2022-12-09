# Definir la función que cambia al estado a zona prohibida
def estadoEliminar():
    global estado
    estado = 1
# Definir la función que cambia el estado a zona de interacción
def estadoInteraccion():
    global estado
    estado = 2
# Definir la función que cambia el estado a zona de trabajo
def estadoTrabajo():
    global estado
    estado = 3
# Definir la función que cambia el estado a vigilancia avanzada
def estadoAvanzado():
    global estado
    global buscandoNombre
    global indetNombre
    estado = 4
    identnameP = EntryName2.get()
    buscandoNombre = not buscandoNombre

# Definición de la maquina de estado y obtencion de la posicion de las zonas
def crearCuadro(event):
    global posInicial
    global posFinal
    global x
    global y
    global estado

    if(estado = 0):
        return
    if(posInicial == False):
        posInicial = {"x":x, "y":y}
    else:
        posFinal = {"x":x, "y":y}
        if(estado != 0):
            if(estado == 1):
                listaDeZonasProhibidas.append(zona(0, posInicial, posFinal))
            if(estado == 2):
                listaDeZonasDeInteraccion.append(zona(0, posInicial, posFinal))
            if(estado == 3):
                listaDeZonasTrabajo.append(zona(0, posInicial, posFinal))
                start = time.time()
            if(estado == 4):
                listaAvanzada.append(zona(0, posInicial, posFinal))

            posInicial =  False
            posFinal = False
            estado = 0

# Activacion de avisos dependiendo del tipo de zona
## Si hay varias personas muy cerca de la zona avisa

