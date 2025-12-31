class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self._contents = [None] * capacity
        self._read_pointer = 0
        self._write_pointer = 0
        self._capacity = capacity

    def read(self):
        if not self._contents[self._read_pointer]:
            raise BufferEmptyException("Circular buffer is empty")
        
        return_value = self._contents[self._read_pointer]
        self._contents[self._read_pointer] = None
        self._increment_read_pointer()

        return return_value

    def write(self, data):
        if self._contents[self._write_pointer]:
            raise BufferFullException("Circular buffer is full")

        self._contents[self._write_pointer] = data
        self._increment_write_pointer()

    def overwrite(self, data):
        if self._contents[self._write_pointer]:
            self._increment_read_pointer()

        self._contents[self._write_pointer] = data
        self._increment_write_pointer()

    def clear(self):
        self._contents = [None] * self._capacity
    
    def _increment_write_pointer(self):
        self._write_pointer = (self._write_pointer + 1) % self._capacity
    
    def _increment_read_pointer(self):
        self._read_pointer = (self._read_pointer + 1) % self._capacity
