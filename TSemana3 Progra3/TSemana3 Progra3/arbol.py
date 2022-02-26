
from Nodo import nodo

Class Arbol:

    def __init__(self, dato)

    def _insertar(self, nodo, dato):
        if dato  < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(dato)
            else:
                self._insertar(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(dato)
                else:
                    self._insertar(nodo.derecho, dato)




