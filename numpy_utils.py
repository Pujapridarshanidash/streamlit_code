import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("\n--Numpy matrix operations---")
A= np.array([[1,2],[3,4]])
B= np.array([[5,6],[7,8]])
print("matrix A:\n",A)
print("matrix B:\n",B)
print("A+B:\n",A+B)
print("A-B:\n",A-B)
print("A*B(element-wise):\n",A*B)
print("A dot B:\n",np.dot(A,B))
#loops
print("\nElements in A greater than 2:")
for i in np.nditer(A):
    if i>2:
        print(i)
    #matplotlib
    print("\n matoltlib plot")
    x=np.linspace(0,10,100)
    y=np.sin(x)
    plt.figure(figsize=(6,4))
    plt.plot()