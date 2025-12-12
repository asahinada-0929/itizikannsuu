import numpy as np

def itizikannsuu():
    a = float(input("傾きを入力"))
    b = float(input("切片を入力"))

    x = np.linspace(-10,10,40)

    y = a * x + b
    return x, y

