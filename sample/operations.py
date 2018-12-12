#!/usr/bin/env python3

from math import *
from evaluate import Evaluate

class Operations:

    position = 0
    result = ''
    memory = ''

    def __init__(self, results, button = ""):
        self.results = results
        self.button = button
        self.evaluate = Evaluate()


    def operation(self):
        if self.button == 'x' :
            self.button = '*'
        self.results.insert(1.0 + Operations.position, self.button)
        Operations.position += 1


    def calculate(self):
        Operations.result = self.getResult()
        result = self.evaluate.eval(Operations.result)
        if (result is None):
            self.setResult(Operations.result)
        else:
            self.setResult(result)


    def delete_all(self):
        self.results.delete(1.0, 'end')


    def add_memory(self):
        Operations.memory = self.results.get(1.0, 'end')
        self.results.delete(1.0, 'end')  


    def display_memory(self):
        self.results.insert(1.0 + (Operations.i/10), Operations.memory) 


    def delete_memory(self):
        Operations.memory = ''


    def delete_last_digit(self):
        Operations.result = self.getResult()
        Operations.result = Operations.result[:-1]
        self.setResult(Operations.result)


    def power2(self):
        Operations.result = self.getResult()
        Operations.result = float(Operations.result)*float(Operations.result)
        self.setResult(Operations.result)
 

    def square_root(self):
        Operations.result = self.getResult()
        Operations.result = sqrt(float(Operations.result))
        self.setResult(Operations.result)


    def plus_minus(self):
        Operations.result = self.getResult()
        Operations.result = float(Operations.result) * (-1)
        self.setResult(Operations.result)

    def getResult(self):
        result = self.results.get(1.0, 'end')
        return result.strip()
    
    def setResult(self, result):
        self.results.delete(1.0, 'end')
        self.results.insert(1.0, result)
