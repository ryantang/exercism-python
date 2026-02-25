class EmptyListException(Exception):
    pass


class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

    def value(self):
        return self._value

    def next(self):
        return self._next

    def set_next(self, next_node):
        self._next = next_node


class LinkedList:
    def __init__(self, values=None):
        if not values:
            self._head = None
            return

        previous_node = None
        for value in values:
            self._head = Node(value)
            self._head.set_next(previous_node)
            previous_node = self._head

        self.node_for_iter = None


    def __iter__(self):
        return self

    def __next__(self):
        if not self._head:
            raise StopIteration

        if not self.node_for_iter:
            self.node_for_iter = self._head
            return self.node_for_iter.value()

        if not self.node_for_iter.next():
            raise StopIteration

        next_node = self.node_for_iter.next()
        self.node_for_iter = next_node

        return next_node.value()


    def __len__(self):
        if not self._head:
            return 0

        length = 1
        current_node = self.head()

        while current_node.next():
            length += 1
            current_node = current_node.next()

        return length


    def head(self):
        if not self._head:
            raise EmptyListException("The list is empty.")

        return self._head

    def push(self, value):
        previous_node = self._head
        self._head = Node(value)
        self._head.set_next(previous_node)

    def pop(self):
        if not self._head:
            raise EmptyListException("The list is empty.")

        removed_node = self._head
        self._head = self._head.next()

        return removed_node.value()

    def reversed(self):
        return LinkedList(list(self))
