from typing import Any

class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int):
        self._contents = [None] * capacity
        self._read_pointer = 0
        self._write_pointer = 0
        self._capacity = capacity

    def read(self) -> Any:
        if self._contents[self._read_pointer] is None:
            raise BufferEmptyException("Circular buffer is empty")
        
        return_value = self._contents[self._read_pointer]
        self._contents[self._read_pointer] = None
        self._read_pointer = self._advance_pointer(self._read_pointer)

        return return_value

    def write(self, data: Any) -> None:
        if self._contents[self._write_pointer] is not None:
            raise BufferFullException("Circular buffer is full")

        self._contents[self._write_pointer] = data
        self._write_pointer = self._advance_pointer(self._write_pointer)

    def overwrite(self, data: Any) -> None:
        if self._contents[self._write_pointer] is not None:
            self._read_pointer = self._advance_pointer(self._read_pointer)

        self._contents[self._write_pointer] = data
        self._write_pointer = self._advance_pointer(self._write_pointer)

    def clear(self) -> None:
        self._contents = [None] * self._capacity
    
    def _advance_pointer(self, pointer: int) -> int:
        return (pointer + 1) % self._capacity
