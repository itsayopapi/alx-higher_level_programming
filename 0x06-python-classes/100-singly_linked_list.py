#!/usr/bin/python3
"""Singly linked list class, in python"""


class Node:
    """Node of a singly linked list"""
    def __init__(self, data=0, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """return data"""
        return self.__data

    @data.setter
    def data(self, value):
        """set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SLL head and functions"""

    def __init__(self):
        self.__head = None

    def __repr__(self):
        retstr = ""
        if self.__head is None:
            pass
        else:
            ptr = self.__head
            while ptr is not None:
                retstr += str(ptr.data) + '\n'
                ptr = ptr.next_node
        return retstr[:-1]

    def sorted_insert(self, value):
        """inserts a linked list node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            ptr = self.__head
            while ptr.next_node is not None and ptr.next_node.data < value:
                ptr = ptr.next_node
            if ptr.next_node is None:
                ptr.next_node = Node(value)
            else:
                ptr.next_node = Node(value, ptr.next_node)
