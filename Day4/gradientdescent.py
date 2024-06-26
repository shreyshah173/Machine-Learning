import numpy as np

np1 = np.array([1, 2, 3,4,5])
np2 = np.array([5,7,9,11,13])

def gradient_descent(x,y):
    m = 2.000000000000002
    b = 2.999999999999995
    n = len(x)
    # m = 0 
    # b = 0
    alpha = 0.0001
    epochs = 100000
    for i in range(epochs):
        yans = m*x + b
        derM = (-2/n) * sum(x * (y - yans))
        derB = (-2/n) * sum(y - yans)
        m = m - alpha * derM
        b = b - alpha * derB
        print("m = ",m," b = ",b," cost = ",(1/n) * sum([val**2 for val in (y - (m*x + b))]))


gradient_descent(np1,np2)