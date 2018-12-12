#!/usr/bin/env python3

from tkinter import *
from keyboard import Keyboard
from operations import Operations

class Calculator:

    def __init__(self):
        self.init_calculator('Calculatrice de la Mort')
        self.init_results()
        self.init_grid()
        self.init_keyboard()
        self.calculator.mainloop()
    

    def init_calculator(self, title):
        self.calculator = Tk()
        self.calculator.title(title)
        self.calculator.resizable(True, True)


    def init_results(self):
        self.results = Text(self.calculator, width=11, height=1, bg='white', bd=2, font="sans 40")
        self.results.grid(row=0, column=0)


    def init_grid(self):
        self.frame = Frame(self.calculator, relief=RAISED, border = 0, bg='white')
        self.frame.grid(row=1, column=0, padx=5, pady=5)


    def init_keyboard(self):
        self.init_simples_commands()
        self.init_specials_commands()


    def init_simples_commands(self):
        button =  ["(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "/", "x", "-", "+", ".", "%"]
        line_column = [[2, 0], [2, 1], [6, 0], [5, 0], [5, 1], [5, 2], [4, 0], [4, 1], [4, 2], [3, 0], [3, 1], [3, 2], [3, 3], [4, 3], [5, 3], [6, 3], [6, 1], [4, 4]]
        command = ""
        for i in range(0, len(button)):
            operation_from_button = Operations(self.results, button[i])
            sign = Keyboard(self.frame, button[i], operation_from_button.operation, line_column[i][0], line_column[i][1])
            sign.add_buttons_signs()


    def init_specials_commands(self):
        operation = Operations(self.results)

        quit = Keyboard(self.frame, "QUITTER", self.calculator.destroy, 1, 0, 16, cospan = 2, bg = '#CECECE')
        quit.add_buttons_signs()
    
        C = Keyboard(self.frame, 'C', operation.delete_all, 1, 2)
        C.add_buttons_signs()
    
        CE = Keyboard(self.frame, 'CE', operation.delete_last_digit, 1, 3)
        CE.add_buttons_signs()
    
        x2 = Keyboard(self.frame, 'x²', operation.power2, 1, 4)
        x2.add_buttons_signs()
    
        MC = Keyboard(self.frame, 'MC', operation.delete_memory, 2, 2)
        MC.add_buttons_signs()
    
        MR = Keyboard(self.frame, 'MR', operation.display_memory, 2, 3)
        MR.add_buttons_signs()
    
        Mplus = Keyboard(self.frame, 'M+', operation.add_memory, 2, 4)
        Mplus.add_buttons_signs()
    
        square = Keyboard(self.frame, '√', operation.square_root, 3, 4)
        square.add_buttons_signs()
    
        egal = Keyboard(self.frame, '=', operation.calculate, 5, 4, height=9, rospan=2)
        egal.add_buttons_signs()
    
        plusMinus = Keyboard(self.frame, '+/-', operation.plus_minus, 6, 2)
        plusMinus.add_buttons_signs()

