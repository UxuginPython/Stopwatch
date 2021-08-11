#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:32:46 2021

@author: benjaminpatterson
"""
from time import time
from tkinter import *

running=False
_time=0
startTime=0

window=Tk()
window.title('Stopwatch - UxuginAI')

def startStopCommand():
    global running
    global startTime
    if running==False:
        startTime=time()
        running=True
        startStop.config(text='Stop')
    elif running==True:
        running=False
        startStop.config(text='Start')
def resetCommand():
    global _time, running
    _time=0
    running=False
    startStop.config(text='Start')
    __time.config(text=str(_time))

startStop=Button(window, text='Start', command=startStopCommand)
reset=Button(window, text='Reset', command=resetCommand)
__time=Label(window, text=str(_time-startTime))

__time.pack()
startStop.pack()
reset.pack()

while True:
    window.update()
    window.update_idletasks()
    if running==True:
        _time=time()
        __time.config(text=str(_time-startTime))