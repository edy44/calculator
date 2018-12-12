#!/usr/bin/env python3

class Evaluate:

    def __init__(self):
        self.formula = []
        self.result = ''
        self.error = False


    def eval(self, expression):
        if (self.percent(expression)):
            return self.result
        if (self.sum(expression)):
            return self.result
        if (self.substract(expression)):
            return self.result
        if (self.multiply(expression)):
            return self.result
        if (self.divide(expression)):
            return self.result
        if (self.error):
            return "Error"
        return None


    def percent(self, expression):
        position = expression.find('%')
        if position != -1:   
            number1 = expression[0:position]
            try:
                self.result = float(number1) / 100
            except:
                self.error = True
                return False
            return True
        return False


    def sum(self, expression):
        position = expression.find('+')
        if position != -1:
            if position == 0:
                number1 = 0
            else:
                number1 = expression[0:position]
            number2 = expression[position+1:len(expression)]
            try:
                self.result = float(number1) + float(number2)
            except:
                self.error = True
                return False
            return True
        return False
    

    def substract(self, expression):
        position = expression.find('-')
        if position != -1:
            if position == 0:
                number1 = 0
            else:
                number1 = expression[0:position]
            number2 = expression[position+1:len(expression)]
            try:
                self.result = float(number1) - float(number2)
            except:
                self.error = True
                return False
            return True
        return False
        

    def multiply(self, expression):
        position = expression.find('*')
        if position != -1:
            number1 = expression[0:position]
            number2 = expression[position+1:len(expression)]
            try:
                self.result = float(number1) * float(number2)
            except:
                self.error = True
                return False
            return True
        return False
    

    def divide(self, expression):
        position = expression.find('/')
        if position != -1:
            number1 = expression[0:position]
            number2 = expression[position+1:len(expression)]
            try:
                self.result = float(number1) / float(number2)
            except:
                self.error = True
                return False
            return True
        return False

