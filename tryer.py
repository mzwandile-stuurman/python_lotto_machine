from math import *
import random
from tkinter import *
from tkinter import messagebox

empty1 =[]

empty2 = []

empty3 = []


while True:

    x=int(input("please select a number: "))
    if len(empty1) <= 5:
        empty1.append(x)

    elif len(empty1) == 6 and len(empty2) <= 6:
        empty2.append(x)
    else:
        empty3.append(x)
        if len(empty3) >=6:
            break

print(empty1, empty2,empty3)
