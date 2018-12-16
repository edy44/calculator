import unittest
from evaluate import *

class TestEvaluate(unittest.TestCase):

    def test_sum(self):
        expression = '3+7'
        sum = Evaluate().sum(expression)
        self.assertTrue(sum)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 10)


    def test_sum_with_one_number(self):
        expression = '+7'
        sum = Evaluate().sum(expression)
        self.assertTrue(sum)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 7)


    def test_substract(self):
        expression = '3-7'
        sub = Evaluate().substract(expression)
        self.assertTrue(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, -4)


    def test_substract_with_one_number(self):
        expression = '-7'
        sub = Evaluate().substract(expression)
        self.assertTrue(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, -7)


    def test_multiply(self):
        expression = '3*7'
        sub = Evaluate().multiply(expression)
        self.assertTrue(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 21)

    
    def test_multiply_with_one_number(self):
        expression = '*7'
        sub = Evaluate().multiply(expression)
        self.assertFalse(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 'Error')


    def test_divide(self):
        expression = '14/7'
        sub = Evaluate().divide(expression)
        self.assertTrue(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 2)


    def test_divide_by_zero(self):
        expression = '14/0'
        sub = Evaluate().divide(expression)
        self.assertFalse(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 'Error')

    
    def test_divide_with_one_number(self):
        expression = '/7'
        sub = Evaluate().divide(expression)
        self.assertFalse(sub)        
        eval = Evaluate().eval(expression)
        self.assertEquals(eval, 'Error')