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
                result = float(number1) / 100
                self.result = self.clear_result(result)
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
                result = float(number1) + float(number2)
                self.result = self.clear_result(result)
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
                result = float(number1) - float(number2)
                self.result = self.clear_result(result)
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
                result = float(number1) * float(number2)
                self.result = self.clear_result(result)
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
            if number2 == '0':
                self.error = True
                return False 
            try:
                result = float(number1) / float(number2)
                self.result = self.clear_result(result)
            except:
                self.error = True
                return False
            return True
        return False


    def clear_result(self, result):
        result = str(result)
        if result[-2:] == '.0':
            return result[:-2]
        return result

