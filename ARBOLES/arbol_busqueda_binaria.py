#### B U S Q U E D A   B I N A R I A   E N   A R B O L E S    B A L A N C E A D O S ####

from __future__ import annotations
from collections.abc import Iterable
from typing import Any

# clase nodo para el arbol binario

class Node:
    def __init__(self, value: int | None = None):
        self.value = value
        self.parent: Node | None = None  # para la eliminacion de nodos mas facil
        self.left: Node | None = None
        self.right: Node | None = None

    # __repr__ es para mostrar el valor del nodo
    def __repr__(self) -> str:
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

# clase arbol binario


class BinarySearchTree:
    def __init__(self, root: Node | None = None):
        # root es el nodo raiz
        self.root = root

    def __str__(self) -> str:
       # Devuelve el arbol en forma de string
        return str(self.root)

    def __reassign_nodes(self, node: Node, new_children: Node | None):
        # vamos a reasignar los nodos de los hijos y padres
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if self.is_right(node):  # If it is the right children
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = None

    def is_right(self, node: Node) -> bool:
        if node.parent and node.parent.right:
            return node == node.parent.right
        return False

    def empty(self) -> bool:
        return self.root is None

    def __insert(self, value) -> None:
        #
        # Insertar  un valor en el arbol
        # creamos un nodo con el valor
        new_node = Node(value)
        #  si el arbol esta vacio, el nodo raiz es el nuevo nodo
        if self.empty():
            self.root = new_node
        # si no esta vacio, buscamos el lugar donde insertar el nodo
        else:
            # empezamos en el nodo raiz y vamos bajando por el arbol
            parent_node = self.root

            if parent_node is None:
                return None

            # mientras no lleguemos a un nodo hoja
            while True:
                if value < parent_node.value:  # si el valor es menor que el nodo actual
                    if parent_node.left is None:
                        parent_node.left = new_node  # insertamos el nuevo nodo a la hoja
                        break

                    else:
                        parent_node = parent_node.left
                # si el valor es mayor que el nodo actual
                else:
                    # si el nodo actual no tiene hijo derecho
                    if parent_node.right is None:
                        # insertamos el nuevo nodo a la hoja
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            # asignamos el padre del nuevo nodo
            new_node.parent = parent_node
    # *args: número de parámetros de entrada puede ser variable

    def insert(self, *values) -> None:
        for value in values:
            self.__insert(value)

    def search(self, value) -> Node | None:
        if self.empty():
            raise IndexError("ERROR: El arbol esta vacio, pon otro valor")
        else:
            # empezamos en el nodo raiz y vamos bajando por el arbol
            node = self.root
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            return node

    def get_max(self, node: Node | None = None) -> Node | None:
        # vamos a buscar el nodo con el valor mas grande
        if node is None:
            # si no se especifica el nodo, empezamos en el nodo raiz
            if self.root is None:
                return None
            node = self.root
        # mientras el nodo tenga un hijo derecho
        if not self.empty():
            while node.right is not None:
                node = node.right
        return node

    def get_min(self, node: Node | None = None) -> Node | None:
        # vamos a buscar el nodo con el valor mas pequeño
        if node is None:
            # si no se especifica el nodo, empezamos en el nodo raiz
            node = self.root
        if self.root is None:
            return None
        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        return node

    def remove(self, value: int) -> None:
        node = self.search(value)
        # si el nodo no tiene hijos
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node, None)
            elif node.left is None:  # hijo derecho
                self.__reassign_nodes(node, node.right)
            elif node.right is None:  # hijo izquierdo
                self.__reassign_nodes(node, node.left)
            else:
                tmp_node = self.get_max(node.left)  #obtenemos el nodo con el valor mas grande del subarbol izquierdo
                self.remove(tmp_node.value)  
                node.value = (tmp_node.value)  # Asignamos el valor del nodo mas grande al nodo que queremos eliminar

    def preorder_traverse(self, node: Node | None) -> Iterable:
        if node is not None:
            # yield es como un return pero no termina la funcion
            # devuelve el valor del nodo y continua con la funcion
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)

    def traversal_tree(self, traversal_function=None) -> Any:
        """
        This function traversal the tree.
        You can pass a function to traversal the tree as needed by client code
        """
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        else:
            return traversal_function(self.root)

    def inorder(self, arr: list, node: Node | None) -> None:
        if node:
            # vamos a recorrer el arbol en orden y lo vamos a guardar en un array 
            # primero el subarbol izquierdo+

            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)

    def find_kth_smallest(self, k: int, node: Node) -> int:
       #  Devuelve el k-ésimo elemento más PEQUEÑO del árbol
       # el array futuramente va  aser  una lista
        arr: list[int] = []
        # Vamos a recorrerlo de menor a mayor y lo vamos a guardar en un array
        self.inorder(arr, node)
        return arr[k - 1]


def postorder(curr_node: Node | None) -> list[Node]:
    # vamos a recorrer el arbol en postorden es decir primero el subarbol izquierdo y luego el derecho
    node_list = []
    if curr_node is not None:
        node_list = postorder(curr_node.left) + \
            postorder(curr_node.right) + [curr_node]
    return node_list


def binary_search_tree() -> None:
    r"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
    >>> t = BinarySearchTree()
    >>> t.insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
    8 3 1 6 4 7 10 14 13
    >>> print(" ".join(repr(i.value) for i in t.traversal_tree(postorder)))
    1 4 7 6 3 13 14 10 8
    >>> BinarySearchTree().search(6)
    Traceback (most recent call last):
        ...
    IndexError: Warning: Tree is empty! please use another.
    """
    # 1. Crear un árbol binario de búsqueda
    # 2. Insertar los valores 8, 3, 6, 1, 10, 14, 13, 4, 7
    # 3. Recorrer el árbol en preorden
    # 4. Recorrer el árbol en postorden
    # 7. Obtener el valor máximo
    # 8. Obtener el valor mínimo
    # ...
    
    testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
    t = BinarySearchTree()
    # añadimos los valores al arbol
    for i in testlist:
        t.insert(i)

    print(t)
    # recorremos el arbol en preorden
    if t.search(6) is not None:
        print("The value 6 exists")
    else:
        print("The value 6 doesn't exist")

    # recorremos el arbol en postorden
    if t.search(-1) is not None:
        print("The value -1 exists")
    else:
        print("The value -1 doesn't exist")
    # obtenemos el valor maximo y  minimo
    if not t.empty():
        print("Max Value: ", t.get_max().value)  # type: ignore
        print("Min Value: ", t.get_min().value)  # type: ignore
    # se elimina de la lista el valor 
    for i in testlist:
        t.remove(i)
        print(t)

# tests

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
