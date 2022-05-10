from copy import deepcopy


class MyQueue:

    def __init__(self):
        self.__stack = []

    @property
    def _size(self):
        return len(self.__stack)

    def _shift(self):
        start = [(self.__stack.pop())]
        _copy = deepcopy(self.__stack)

        self.__stack = start
        self.__stack.extend(_copy)

    def push(self, x: int, shift=True) -> None:
        self.__stack.append(x)
        if shift:
            self._shift()

    def pop(self) -> int:
        return self.__stack.pop()

    def peek(self) -> int:
        val = self.__stack.pop()
        self.push(val, shift=False)
        return val

    def empty(self) -> bool:
        return True if self._size == 0 else False
