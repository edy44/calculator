#!/usr/bin/env python3

from tkinter import *

class Keyboard:

    def __init__(self, frame, sign, command, line, column, 
    width = 6, height = 4, border = 1, relief='raised', rospan = 1, cospan = 1, bg = '#CECECE'):
        self.frame = frame  
        self.sign = sign 
        self.command = command
        self.line = line
        self.column = column
        self.width = width
        self.height = height
        self.border = border
        self.relief = relief
        self.rospan = rospan
        self.cospan = cospan
        self.bg = bg
  
    def add_buttons_signs(self):
        Button(self.frame, text = self.sign, width = self.width, height = self.height, relief = self.relief, border = self.border, command = self.command, bg = self.bg).grid(row = self.line, column = self.column, rowspan = self.rospan, columnspan = self.cospan)