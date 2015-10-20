#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pyboard
-------------------------------------------------

A onscreen/virtual keyboard

author: Claude Müller
"""

from tkinter import Tk, BOTH, LEFT, TOP, Button
from tkinter.ttk import Frame, Style #, Button
import json
import collections
from pprint import pprint

class Pyboard(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        # Set window width and height
        self.windowWidth = self.parent.winfo_screenwidth()
        self.windowHeight = self.parent.winfo_screenheight() / 3
        # As well as position on screen (bottom)
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
        # Extract the json object from the us.json file
        with open("us.json") as keyboardLayout:
            layout = json.load(keyboardLayout)

        rows = []
        i = 0
        left = True

        buttonHeight = self.windowHeight / len(layout)

        # pprint(type(layout))
        sortedLayout = collections.OrderedDict(sorted(layout.items()))

        # Iterate over each row in layout
        for row in sortedLayout:
            keys = []

            # Frame for the current row
            rowKeys = Frame(self)
            rowKeys.pack(side = TOP)

            # For each key in current row
            for key in sortedLayout[row]:
                tempKey = {
                        "key": key['key'],
                        "btn": Button(rowKeys, text = key['key'], command=self.passingBy, height=4, width=15)
                        }
                if left:
                    stack = LEFT
                else:
                    stack = TOP

                tempKey["btn"].pack(side=stack)

                # Append key to rows's keys
                keys.append(tempKey)

            # Append keys of row to actual row
            rows.append(rowKeys)
            stack = False

    def passingBy(self):
        pass


if __name__ == "__main__":
    root = Tk()
    app = Pyboard(root)
    root.mainloop()
