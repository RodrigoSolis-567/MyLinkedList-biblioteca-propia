Este es mi primera libreria que creo, no es perfecta ni mucho menos, pero por algo se empieza, ni siquiera la subi a pypí u otro lugar de forma online por falta de tiempo

# MyLinkedList

Una estructura de datos en Python que combina una lista posicional basada en índices con una red de nodos multilazados.

## Cómo instalarlo

* Coloca el archivo `MyLinkedList.py` junto con un archivo `setup.py` en una carpeta separada de tus proyectos.
* Abre la terminal en dicha carpeta y ejecuta el comando de instalación en modo desarrollador dentro
  de la terminal del IDE:

  "pip install -e ."

## Cómo llamarlo
para llamarlo debes escribir en la parte superiro de tu codigo els siguiente Script

    from MyLinkedList import MyLinkedList

## Funciones de Métodos

| Método / Indexador        | Descripción |
| :---                      | :---        |
| `insertAt(index, valor)`  | Inserta un valor en la posición dada (rellena con `None` si hay salto). |
| `replaceAt(index, valor)` | Reemplaza o crea un nodo en la posición exacta.                         |
| `insertFront(valor)`      | Inserta un nodo al inicio de la lista (posición `0`).                   |
| `insertEnd(valor)`        | Inserta un nodo al final de la lista.                                   |
| `linkPositions(p1, p2)`   | Enlaza el nodo origen (`p1`) con el nodo destino (`p2`) usando índices. |
| `LinkSearch[index]`       | Indexador para obtener el nodo en una posición específica.              |
| `delate[index]`           | Indexador GET para eliminar y reajustar la lista.                       |
| `delate[index] = None`    | Indexador SET para anular un nodo dejándolo como `None`.                |
| `viewLinkedList()`        | Imprime en consola el estado actual de la red y sus conexiones.         |
