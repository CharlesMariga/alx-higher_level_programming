#!/usr/bin/python3
"""Defines a class Node"""


class Node:
    def __init__(self, data, next_node=None):
        """Initializes the node

        Args:
            data (int): data for the node
            next_node (Node): node pointer
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Retrives the data private field

        Returns:
            The value of the data private field
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data private field

        Args:
            value: value of the node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Retrieves next node

        Returns:
            The value of the next_node pointer
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the value of the next_node

        Args:
            value: value of the next node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a SinglyList class"""


class SinglyLinkedList:
    def __init__(self):
        """Initializes the SinglyLinkedList instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Prints the singly list object

        Returns:
            print the singly linke list
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)
