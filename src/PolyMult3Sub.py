import time
import numpy as np
from random import randint, random
import time
import matplotlib.pyplot as plt

# Polynomial Multiplication High School Algorithm
def PMHighSchool(P, Q):
    n = len(P)
    PQ = np.zeros(n*2)
    for i in range(0, n):
        for j in range(0, n):
            PQ[i+j] += P[i] * Q[j]
    return PQ


# Polynomial Multiplication Divide and Conquer Algorithm
def PMDivConq4Sub(P, Q, n):
    PQ = np.zeros(int(n)*2)
    if n == 1:
        PQ[0] = P[0]*Q[0]
        return PQ
    PQ_LL = PMDivConq4Sub(P[0:int(n/2)], Q[0:int(n/2)], int(n/2))
    PQ_LH = PMDivConq4Sub(P[0:int(n/2)], Q[int(n/2):], int(n/2))
    PQ_HL = PMDivConq4Sub(P[int(n/2):], Q[0:int(n/2)], int(n/2))
    PQ_HH = PMDivConq4Sub(P[int(n/2):], Q[int(n/2):], int(n/2))
    # Solution construction step
    for i in range(0, n):
        PQ[i] += PQ_LL[i]
        PQ[i+int(n/2)] += PQ_LH[i]
        PQ[i+int(n/2)] += PQ_HL[i]
        PQ[i+n] += PQ_HH[i]
    return PQ


# Polynomial Multiplication Divide and Conquer Algorithm
def PMDivConq3Sub(P, Q, n):
    PQ = np.zeros(int(n)*2)
    # Base case, when size is 1, just return P[0]*Q[0]
    if n == 1:
        PQ[0] = P[0]*Q[0]
        return PQ
    PQ_LL = PMDivConq3Sub(P[0:int(n/2)], Q[0:int(n/2)], int(n/2))
    PQ_HH = PMDivConq3Sub(P[int(n/2):], Q[int(n/2):], int(n/2))
    PQ_M = PMDivConq3Sub()

    # Solution construction step
    for i in range(0, n):
        PQ[i] += PQ_LL[i]
        PQ[i+int(n/2)] += PQ_LH[i]
        PQ[i+int(n/2)] += PQ_HL[i]
        PQ[i+n] += PQ_HH[i]
    return PQ


def probGen(n):
    P = np.zeros((10, n))
    Q = np.zeros((10, n))
    for j in range(0, 10):
        for i in range(0, n):
            P[j][i] = float(random())
            Q[j][i] = float(random())
    return P, Q


# Function to create a logarithmic y-axis plot for runtimes
def loglogPlot2(x, y1, y2, y3):
    plt.plot(x, y1, label="HS")
    plt.plot(x, y2, label="4Sub")
    plt.plot(x, y3, label="3Sub")
    plt.xlabel("Problem size")
    plt.ylabel("Run time (s)")
    plt.yscale("log")
    plt.xscale("log")
    plt.title("Log-Log Plot of Problem Size v Run Time")
    plt.legend()
    plt.show()


def main():
    # Testing the 3 sub problem algorithm
    P = [2, 1, 1, 0]
    Q = [3, 1, 1, 0]
    PQ = PMDivConq3Sub(P, Q, len(P))
    for i in range(len(PQ)-2, -1, -1):
        print(f"{float(PQ[i])}*x^{i}", end="")
        if i-1 != -1:
            print(" + ", end="")
    print()
    print()

    # Testing the 3 sub problem algorithm with larger data set
    n = 2**randint(1, 4)
    P = []
    Q = []
    for i in range(0, n):
        P.append(randint(0, 20))
        Q.append(randint(0, 20))
    PQ = PMHighSchool(P, Q)
    print("High School:")
    for i in range(len(PQ)-2, -1, -1):
        print(f"{float(PQ[i])}*x^{i}", end="")
        if i-1 != -1:
            print(" + ", end="")
    print()
    print()

    # Generating a problem and timing the three algorithms
    n = 2**4
    maxN = 2**7
    nCount = np.zeros(maxN+1)
    runtimeHS = np.zeros(maxN+1)
    runtimeDC = np.zeros(maxN+1)
    runtime3S = np.zeros(maxN + 1)  # 3 sub problem run time
    while n <= maxN:
        nCount[n] = n
        [P, Q] = probGen(n)
        start = time.time()
        for i in range(0, 10):
            PMHighSchool(P[i], Q[i])
        end = time.time()
        runtimeHS[n] = end - start
        start = time.time()
        for i in range(0, 10):
            PMDivConq4Sub(P[i], Q[i], n)
        end = time.time()
        runtimeDC[n] = end - start
        start = time.time()
        for i in range(0, 10):
            PMDivConq3Sub(P[i], Q[i], n)
        end = time.time()
        runtime3S[n] = end - start

        n *= 2

    f = open("TestTiming.txt", 'w')
    f.truncate(0)
    f.write(f"P:{str(P)}")
    f.write(f"Q:{str(Q)}")

    loglogPlot2(nCount, runtimeHS, runtimeDC, runtime3S)


main()
