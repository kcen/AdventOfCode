from inspect import signature
from collections import namedtuple


def arity(func):
    return len(signature(func).parameters)


ItemContainer = namedtuple("ItemContainer", ["get", "set"])


class Computer:
    def __init__(self, input):
        self.opcodes = {
            1: self.add,
            2: self.mult,
            3: self.write,
            4: self.read,
            5: self.jmp_true,
            6: self.jmp_false,
            7: self.less_than,
            8: self.equals,
            99: self.end,
        }
        self.data_map = list(map(int, open("input").read().split(",")))
        self.cursor = 0
        self.memory = [input]

    def _addressobj_(self, location):
        def getter():
            return self.data_map[location]

        def setter(value):
            self.data_map[location] = value
            return getter()

        return ItemContainer(getter, setter)

    def _valueobj_(self, value):
        def getter():
            return value

        def setter(*args):
            raise NotImplementedError

        return ItemContainer(getter, setter)

    def run(self):
        try:
            while self.cursor < len(self.data_map):
                opcode, *args = self.next_exec()
                opcode(*args)

        except StopIteration:
            print(f"Final Memory Result: {self.memory}")
        return self.data_map[0]

    def add(self, item1, item2, item3):
        item3.set(item1.get() + item2.get())

    def mult(self, item1, item2, item3):
        item3.set(item1.get() * item2.get())

    def read(self, item):
        self.memory.append(item.get())

    def write(self, item):
        item.set(self.memory.pop())

    def jmp_true(self, cond_item, item):
        if cond_item.get():
            self.cursor = item.get()

    def jmp_false(self, cond_item, item):
        if not cond_item.get():
            self.cursor = item.get()

    def less_than(self, item1, item2, item3):
        item3.set(int(item1.get() < item2.get()))

    def equals(self, item1, item2, item3):
        item3.set(int(item1.get() == item2.get()))

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


Computer(input=5).run()
