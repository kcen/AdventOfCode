from inspect import signature
from collections import namedtuple


def arity(func):
    return len(signature(func).parameters)


ValueContainer = namedtuple("ValueContainer", ["get", "set"])


class Computer:
    def __init__(self, input):
        self.opcodes = {1: self.add, 2: self.mult, 3: self.write, 4: self.read, 99: self.end}
        self.data_map = list(map(int, open("input").read().split(",")))
        self.cursor = 0
        self.memory = [input]

    def _addressobj_(self, location):
        def getter():
            return self.data_map[location]

        def setter(value):
            self.data_map[location] = value
            return getter()

        return ValueContainer(getter, setter)

    def _valueobj_(self, value):
        def getter():
            return value

        def setter(*args):
            raise NotImplementedError

        return ValueContainer(getter, setter)

    def run(self):
        try:
            while self.cursor < len(self.data_map):
                opcode, *args = self.next_exec()
                opcode(*args)

        except StopIteration:
            pass
        print(f"Final Memory Result: {self.memory}")
        return self.data_map[0]

    def add(self, address1, address2, address3):
        address3.set(address1.get() + address2.get())

    def mult(self, address1, address2, address3):
        address3.set(address1.get() * address2.get())

    def read(self, address):
        self.memory.append(address.get())

    def write(self, address):
        address.set(self.memory.pop())

    def end(self):
        raise StopIteration()

    def next_exec(self):
        *abc, d, e = str(self.data_map[self.cursor]).rjust(5)
        cba = abc[::-1]  # Reverse
        self.cursor += 1
        opcode = self.opcodes[int(d + e)]

        args = []
        for _ in range(arity(opcode)):
            cell_value = self.data_map[self.cursor]
            tp = cba.pop(0)
            if tp == "1":  # Immediate mode
                arg = self._valueobj_(cell_value)
            else:  # Position Mode
                arg = self._addressobj_(cell_value)
            args.append(arg)
            self.cursor += 1
        return [opcode, *args]


Computer(input=1).run()
