#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Pyboard
    -------------------------------------------------

    A onscreen/virtual keyboard

    author: Claude Müller

"""

from tkinter import Tk, BOTH, LEFT, TOP
from ttk import Frame, Button, Style
import json
from pprint import pprint

class Pyboard(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.windowWidth = self.parent.winfo_screenwidth()
        self.windowHeight = self.parent.winfo_screenheight() / 3
        self.windowX = 0
        self.windowY = self.parent.winfo_screenheight() - self.windowHeight

        self.initUI()

    def initUI(self):
        self.parent.title("Pyboard onscreen keyboard")
        self.style = Style()
        self.style.theme_use("default")

        self.pack(fill = BOTH, expand = 1)
        self.parent.geometry("%dx%d+%d+%d" % (self.windowWidth, self.windowHeight, self.windowX, self.windowY))

        self.addButtons()

    def addButtons(self):
        with open("us.json") as keyboardLayout:
            layout = json.load(keyboardLayout)

        rows = []
        i = 0
        left = True

        buttonHeight = self.windowHeight / len(layout)

        for row in layout:
            keys = []
            rowKeys = Frame(self)
            rowKeys.pack(side = TOP)
            for key in row:
                tempKey = {
                        "key": key,
                        "btn": Button(rowKeys, text = key, command = self.passingBy) #, height = buttonHeight)
                        }
                if left:
                    stack = LEFT
                else:
                    stack = TOP

                tempKey["btn"].pack(side = stack)
                keys.append(tempKey)
            rows.append(rowKeys)
            stack = False

        pprint(rows)

    def passingBy(self):
        pass


if __name__ == "__main__":
    root = Tk()
    app = Pyboard(root)
    root.mainloop()
