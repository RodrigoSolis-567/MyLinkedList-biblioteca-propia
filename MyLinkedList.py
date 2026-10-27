class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguientes = []  # Soporta múltiples enlaces a otros nodos por posición

    def __repr__(self):
        return f"Nodo({self.valor})"


class _DeleteIndexer:
    """Clase auxiliar para manejar el borrado mediante .delate[index]"""
    def __init__(self, lista_enlazada):
        self.lista_enlazada = lista_enlazada

    def __getitem__(self, index):
        """Permite borrar el elemento y recorrer/ajustar la lista: .delate[indice]"""
        return self.lista_enlazada.delete(index) # O _eliminar_y_recorrer si lo tenías así

    def __setitem__(self, index, value):
        """Permite cambiar el valor de una posición a None: .delate[indice] = None"""
        if value is not None:  # Limpiamos la condición duplicada
            raise ValueError("Solo se puede asignar 'None' en esta operación de borrado por asignación.")
        # AQUÍ ESTABA EL ERROR: Llamamos a deleteNull en lugar de _cambiar_a_null
        self.lista_enlazada.deleteNull(index)


class _LinkIndexer:
    """Clase para buscar elementos exclusivamente por posición usando corchetes: LinkSearch[index]"""
    def __init__(self, lista_enlazada):
        self.lista_enlazada = lista_enlazada

    def __getitem__(self, index):
        secuencia = self.lista_enlazada.secuencia_lineal()
        if not (-len(secuencia) <= index < len(secuencia)):
            raise IndexError("Índice fuera del rango de la lista enlazada.")
        return secuencia[index]


class MyLinkedList:
    def __init__(self):
        # La lista ahora se rige puramente por un arreglo posicional interno
        self._nodos = []
        # Buscador estricto por posición con corchetes
        self.LinkSearch = _LinkIndexer(self)
        # Sistema de borrado con corchetes
        self.delate = _DeleteIndexer(self)

    def secuencia_lineal(self):
        """Retorna la secuencia actual de nodos ordenada por posición."""
        return self._nodos

    def insertAt(self, index, valor):
        """
        Inserta un valor en una posición específica. 
        Si el índice está fuera del límite actual, rellena los espacios vacíos con None (None).
        """
        # Si el índice es mayor al tamaño actual, rellenamos con None hasta alcanzarlo
        while len(self._nodos) < index:
            self._nodos.append(None)

        nuevo_nodo = Nodo(valor) if valor is not None else None
        
        if index >= len(self._nodos):
            self._nodos.append(nuevo_nodo)
        else:
            self._nodos.insert(index, nuevo_nodo)

    def replaceAt(self, index, nuevo_valor):
        """
        Reemplaza o sobrescribe el nodo en una posición específica por uno nuevo.
        Si la posición supera el límite actual, rellena con None hasta ese índice.
        """
        if index < 0:
            raise IndexError("El índice no puede ser negativo.")

        # Rellenar con None si el índice está fuera del rango actual
        while len(self._nodos) <= index:
            self._nodos.append(None)

        # Sobrescribimos el valor en la posición dada
        self._nodos[index] = Nodo(nuevo_valor) if nuevo_valor is not None else None

    def insertFront(self, valor):
        """Inserta al principio (posición 0)."""
        nuevo_nodo = Nodo(valor) if valor is not None else None
        self._nodos.insert(0, nuevo_nodo)

    def insertEnd(self, valor):
        """Inserta al final de la lista."""
        nuevo_nodo = Nodo(valor) if valor is not None else None
        self._nodos.append(nuevo_nodo)

    def linkPositions(self, pos_origen, pos_destino):
        """Crea un enlace entre dos nodos utilizando exclusivamente sus posiciones numéricas."""
        if not (0 <= pos_origen < len(self._nodos) and 0 <= pos_destino < len(self._nodos)):
            raise IndexError("Una o ambas posiciones especificadas están fuera de rango.")
        
        origen = self._nodos[pos_origen]
        destino = self._nodos[pos_destino]

        if origen is None or destino is None:
            raise ValueError("No se puede enlazar una posición que contiene 'None'.")

        if destino not in origen.siguientes:
            origen.siguientes.append(destino)

    def delete(self, index):
        """Elimina el nodo en la posición dada y recorre la lista para ajustar (sin dejar huecos)."""
        if 0 <= index < len(self._nodos):
            return self._nodos.pop(index)
        raise IndexError("Índice fuera del rango para eliminar.")

    def deleteNull(self, index):
        """Reemplaza el elemento en la posición dada por None (None) manteniendo la estructura."""
        if 0 <= index < len(self._nodos):
            self._nodos[index] = None
        else:
            raise IndexError("Índice fuera del rango.")

    def viewLinkedList(self):
        print("\n--- Estado de la Lista Enlazada / Red (Por Posición) ---")
        for idx, nodo in enumerate(self._nodos):
            if nodo is None:
                print(f"Posición [{idx}] ---> None")
            else:
                destinos = [s.valor for s in nodo.siguientes if s is not None]
                print(f"Posición [{idx}] (Valor: {nodo.valor})  --->  Conecta con: {destinos}")
        print("-------------------------------------------------------\n")