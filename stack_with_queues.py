class MyStack:

    def __init__(self):
        self.__queue = []
        self._top = None

    def _shift(self, n):
        for i in range(n):
            self._push_to_back(self._pop_from_front())

    def _size(self) -> int:
        return len(self.__queue)

    def _push_to_back(self, x):
        self.__queue.append(x)

    def _pop_from_front(self):
        if self.__queue:
            return self.__queue.pop(0)

    def push(self, x: int) -> None:
        if x:
            self._push_to_back(x)
            self._shift(self._size() - 1)
            self._top = x

    def pop(self) -> int:
        val = self._pop_from_front()
        self.push(self._pop_from_front())
        return val

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        print(self.__queue)
        return True if self._size() == 0 else False
