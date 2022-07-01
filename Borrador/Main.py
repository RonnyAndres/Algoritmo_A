# Importar State de Estado.py
import copy
from Estado import State
from ListPriorityOpen import ListPriority

# Definir estado inicial y final
estadoInicial = State([4,3],[1,2],[],None)
estadoFinal = State([],[],[4,3,2,1],None)



# Crear lista de estados
listaAbiertos = ListPriority()
listaCerrados = []

# Guardar estado inicial en lista de estados abiertos
listaAbiertos.insert(estadoInicial)


# Funcion crear nuevo estado 
def crearNuevosEstados(estado):
 
    states = []
    
    # Apilar de A a B 
    if len(estado.PilaA) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaB.append(nuevoEstado.PilaA.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)

    # Apilar de A a C
    if len(estado.PilaA) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaC.append(nuevoEstado.PilaA.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)

    # Apilar de B a A
    if len(estado.PilaB) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaA.append(nuevoEstado.PilaB.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)
    
    # Apilar de B a C
    if len(estado.PilaB) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaC.append(nuevoEstado.PilaB.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)
    
    # Apilar de C a A
    if len(estado.PilaC) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaA.append(nuevoEstado.PilaC.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)

    # Apilar de C a B
    if len(estado.PilaC) > 0:
        nuevoEstado = copy.deepcopy(estado)
        nuevoEstado.PilaB.append(nuevoEstado.PilaC.pop())
        estadoCreado = State(nuevoEstado.PilaA, nuevoEstado.PilaB, nuevoEstado.PilaC, estado)
        states.append(estadoCreado)
        listaAbiertos.insert(estadoCreado)   
    

for i in range(15):
    estadoActual = listaAbiertos.returnLast()
    print("Estado Actual:", estadoActual.VH, estadoActual.PilaA, estadoActual.PilaB, estadoActual.PilaC)
    # Verificar si el estado actual es el estado final con VH
    

    # Consultar si el estado inicial no esta en la lista de cerrados
    if estadoActual not in listaCerrados:
        # Crear nuevos estados
        crearNuevosEstados(estadoActual)
        # Guardar estado actual en lista de cerrados
        listaCerrados.append(estadoActual)
        # Eliminar estado actual de lista de abiertos
        listaAbiertos.remove(estadoActual)
    # Si el estado actual es el estado final

