from typing import Any
from collections.abc import Iterable


class EmptyListException(Exception):
    """Exception raised when performing an operation on an empty linked list."""



class Node:
    """A node in a singly linked list."""

    def __init__(self, value: Any) -> None:
        """Initialize a node with a value and optional next node."""
        self._value = value
        self._next = None

    def value(self) -> Any:
        """Return the value stored in this node."""
        return self._value

    def next(self) -> "Node | None":
        """Return the next node, or None if this is the last node."""
        return self._next

    def set_next(self, next_node: "Node | None") -> None:
        """Set the next node reference."""
        self._next = next_node


class LinkedListIterator:
    """Iterator for the LinkedList class."""

    def __init__(self, linked_list: "LinkedList") -> None:
        """Initialize the iterator with a reference to the linked list."""
        self.linked_list = linked_list
        self.node_for_iter = None
        if not self.linked_list.is_empty():
            self.node_for_iter = linked_list.head()

    def __iter__(self) -> "LinkedListIterator":
        """Return the iterator itself."""
        return self

    def __next__(self) -> Any:
        """Return the next value in the linked list, or raise StopIteration."""
        if not self.node_for_iter:
            raise StopIteration
        next_node = self.node_for_iter
        self.node_for_iter = self.node_for_iter.next()
        return next_node.value()




class LinkedList:
    """A singly linked list supporting push, pop, iteration, and reversal."""

    def __init__(self, values: Iterable[Any] | None = None) -> None:
        """Initialize the linked list with optional values."""
        if not values:
            self._head = None
            return

        previous_node = None
        for value in values:
            self._head = Node(value)
            self._head.set_next(previous_node)
            previous_node = self._head


    def __iter__(self) -> "LinkedListIterator":
        """Return an iterator for the linked list."""
        return LinkedListIterator(self)



    def __len__(self) -> int:
        """Return the number of elements in the linked list."""
        if not self._head:
            return 0
        length = 1
        current_node = self.head()
        while current_node.next():
            length += 1
            current_node = current_node.next()
        return length



    def head(self) -> "Node":
        """Return the head node of the linked list, or raise if empty."""
        if self.is_empty():
            raise EmptyListException("The list is empty.")
        return self._head


    def push(self, value: Any) -> None:
        """Push a value onto the head of the linked list."""
        previous_node = self._head
        self._head = Node(value)
        self._head.set_next(previous_node)


    def pop(self) -> Any:
        """Remove and return the value at the head of the linked list."""
        if self.is_empty():
            raise EmptyListException("The list is empty.")
        removed_node = self._head
        self._head = self._head.next()
        return removed_node.value()


    def reversed(self) -> "LinkedList":
        """Return a new linked list with the elements reversed."""
        return LinkedList(list(self))


    def is_empty(self) -> bool:
        """Return True if the linked list is empty, False otherwise."""
        return not self._head
