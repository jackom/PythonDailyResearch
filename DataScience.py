import numpy as np
import matplotlib.pyplot as plt

print("交叉熵公式 START")


def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    print("Y is: ", Y)
    print("P is: ", P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log((1 - P)))


ce = cross_entropy([1, 1, 0], [0.8, 0.7, 0.1])
print(ce)

print("交叉熵公式 END")


