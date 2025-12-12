import numpy as np

def nizikannsuu():
    print("y=a*x*x+b*x+c")
    a = float(input("aを入力"))
    b = float(input("bを入力"))
    c = float(input("cを入力"))
    

    x = np.linspace(-10,10,40)

    y = a * x * x + b*x + c
    return x, y
