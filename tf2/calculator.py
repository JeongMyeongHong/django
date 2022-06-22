import tensorflow as tf
from dataclasses import dataclass
from icecream import ic
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


@dataclass
class Machine(object):
    def __init__(self):
        self._num1 = 0.0
        self._num2 = 0.0

    @property
    def num1(self) -> float: return self._num1

    @num1.setter
    def num1(self, value): self._num1 = value

    @property
    def num2(self) -> float: return self._num2

    @num2.setter
    def num2(self, value): self._num2 = value


class Solution:
    def __init__(self, payload):
        self._num1 = payload.num1
        self._num2 = payload.num2

    @tf.function
    def add(self):
        return tf.add(self._num1, self._num2)

    @tf.function
    def sub(self):
        return tf.subtract(self._num1, self._num2)

    @tf.function
    def mul(self):
        return tf.multiply(self._num1, self._num2)

    @tf.function
    def div(self):
        return tf.divide(self._num1, self._num2)


class UseModel:
    def __init__(self):
        pass

    @staticmethod
    def calc(num1, num2, opcode):
        model = Machine()
        model.num1 = num1
        model.num2 = num2
        solution = Solution(model)
        if opcode == '+':
            result = solution.add()
        elif opcode == '-':
            result = solution.sub()
        elif opcode == '*':
            result = solution.mul()
        elif opcode == '/':
            result = solution.div()
        else:
            result = 'error'

        return result


if __name__ == '__main__':
    num1 = 10
    num2 = 2
    opcodes = ['+', '-', '*', '/']
    [ic(UseModel.calc(num1=num1, num2=num2, opcode=opcode)) for opcode in opcodes]
