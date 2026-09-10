class Node:
    ''' A node of a linked list, with pointers to the previous and subsquent nodes '''
    def __init__(self, value, succeeding=None, previous=None):
        self.prev = previous
        self.next = succeeding
        self.value = value


class LinkedList:
    '''A linked list comprised of nodes, a head pointer, a tail pointer, and a count of nodes '''
    def __init__(self):
        self.head = None
        self.tail = None
        self._count = 0

    def __len__(self):
        return self._count


    def delete(self, value: any) -> None:
        ''' Remove the node whose value matches the passed in value '''
        if self._count == 0:
            raise ValueError('Value not found')

        node = self.head
        while node:
            if node.value == value:
                self._remove_node(node)
                return
            node = node.next

        raise ValueError('Value not found')

    def _remove_node(self, node: Node) -> None:
        ''' Helper function that properly removes a node in the linked list '''
        if self._count == 1 and (self.head != node or self.tail != node):
            raise ValueError('Structure of linked list incorrect')

        if self._count == 1:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None
        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            predecessor_node = node.prev
            successor_node = node.next
            predecessor_node.next = successor_node
            successor_node.prev = predecessor_node

        self._count -=1


    def push(self, value: any) -> None:
        ''' Adds a node with the given value at the end of the list.'''
        new_node = Node(value)

        if self._count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            penultimate_node = self.tail
            self.tail = new_node

            penultimate_node.next = new_node
            new_node.prev = penultimate_node

        self._count += 1


    def pop(self) -> None:
        ''' Removes the node at the end of the list.'''
        if self._count == 0:
            raise IndexError('List is empty')

        value = self.tail.value
        self._remove_node(self.tail)
        return value


    def shift(self):
        ''' Adds a node with the given value at the beginning of the list.'''
        if self._count == 0:
            raise IndexError('List is empty')

        value = self.head.value
        self._remove_node(self.head)
        return value


    def unshift(self, value: any) -> None:
        ''' Removes the node at the beginning of the list. '''
        new_node = Node(value)

        if self._count == 0:
            self.head = new_node
            self.tail = new_node
        else:
            second_node = self.head
            self.head = new_node

            second_node.prev = new_node
            new_node.next = second_node

        self._count += 1
