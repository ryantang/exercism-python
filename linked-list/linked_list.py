"""Doubly linked list implementation."""
from __future__ import annotations
import dataclasses
from typing import Any
from collections.abc import Iterator

@dataclasses.dataclass
class Node:
    """A node of a linked list, with pointers to the previous and subsequent nodes."""
    value: Any
    prev: Node = None
    next: Node = None


class LinkedList:
    """A linked list comprised of nodes, a head pointer, a tail pointer, and a count of nodes."""
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self._count = 0

    def __len__(self) -> int:
        return self._count

    def __iter__(self) -> Iterator[Node]:
        """Iterate over nodes, and not values."""
        node = self.head
        while node:
            yield node
            node = node.next

    @property
    def _empty(self) -> bool:
        return not self._count

    def delete(self, value: Any) -> None:
        """Remove the node whose value matches the passed in value."""
        for node in self:
            if node.value == value:
                self._remove_node(node)
                return

        raise ValueError('Value not found')

    def _remove_node(self, node: Node) -> None:
        """Handles special cases for node removal."""
        if self._count == 1:
            assert node is self.head is self.tail, "single-node list is inconsistent"
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            predecessor_node = node.prev
            successor_node = node.next
            predecessor_node.next = successor_node
            successor_node.prev = predecessor_node

        self._count -= 1


    def push(self, value: Any) -> None:
        """Adds a node with the given value at the end of the list."""
        new_node = Node(value)

        if self._empty:
            self.head = new_node
            self.tail = new_node
        else:
            old_tail = self.tail
            self.tail = new_node

            old_tail.next = new_node
            new_node.prev = old_tail

        self._count += 1


    def pop(self) -> Any:
        """Removes the node at the end of the list and returns its value."""
        if self._empty:
            raise IndexError('List is empty')

        value = self.tail.value
        self._remove_node(self.tail)
        return value


    def shift(self) -> Any:
        """Removes the node at the beginning of the list and returns its value."""
        if self._empty:
            raise IndexError('List is empty')

        value = self.head.value
        self._remove_node(self.head)
        return value


    def unshift(self, value: Any) -> None:
        """Adds a node with the given value at the beginning of the list."""
        new_node = Node(value)

        if self._empty:
            self.head = new_node
            self.tail = new_node
        else:
            old_head = self.head
            self.head = new_node

            old_head.prev = new_node
            new_node.next = old_head

        self._count += 1
