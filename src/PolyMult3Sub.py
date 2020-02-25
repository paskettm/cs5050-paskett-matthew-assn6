import time
import numpy as np
from random import randint, random
import time
import matplotlib.pyplot as plt
import sys

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
    # Dividing the problem into 3 sub problems AND CONQUERING
    PQ_LL = PMDivConq3Sub(P[0:int(n/2)], Q[0:int(n/2)], int(n/2))
    PQ_HH = PMDivConq3Sub(P[int(n/2):], Q[int(n/2):], int(n/2))
    PQ_ML = []
    PQ_MH = []
    for i in range(int(n/2)):
        PQ_ML.append(P[i] + P[i+int(n/2)])
        PQ_MH.append(Q[i] + Q[i+int(n/2)])
    PQ_M = PMDivConq3Sub(PQ_ML, PQ_MH, int(n/2))
    # Solution construction step
    for i in range(0, n):
        PQ[i] += PQ_LL[i]
        PQ[i+n] += PQ_HH[i]
        PQ[i+int(n/2)] += PQ_M[i] - PQ_LL[i] - PQ_HH[i]
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
# and calculate slopes and offsets
def loglogPlot3(x, y1, y2, y3):
    # Creating loglog graph of 3 algos
    plt.plot(x, y1, label="HS")
    plt.plot(x, y2, label="4Sub")
    plt.plot(x, y3, label="3Sub")
    plt.xlabel("Problem size")
    plt.ylabel("Run time (s)")
    plt.yscale("log")
    plt.xscale("log")
    plt.title("Log-Log Plot of Problem Size v Run Time")
    plt.legend()
    plt.savefig("loglog.png")
    # Using numpy.polyfit to find slope and intercept of loglog graphs
    degree = 1
    slopeHS, interceptHS = np.polyfit(np.log(x), np.log(y1), degree)
    slope4S, intercept4S = np.polyfit(np.log(x), np.log(y2), degree)
    slope3S, intercept3S = np.polyfit(np.log(x), np.log(y3), degree)
    return slopeHS, interceptHS, slope4S, intercept4S, slope3S, intercept3S


def main():
    # Testing the 3 sub problem algorithm
    print("Checking the values of a small problem using the 3 sub problem algo:")
    P = [2, 1, 1, 0]
    Q = [3, 1, 1, 0]
    PQ = PMDivConq3Sub(P, Q, len(P))
    for i in range(len(PQ)-2, -1, -1):
        print(f"{float(PQ[i])}*x^{i}", end="")
        if i-1 != -1:
            print(" + ", end="")
    print()
    print()

    # Testing the 3 sub problem against high school
    print("Checking that 3 sub gives same output as high school:")
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
    PQ = PMDivConq3Sub(P, Q, n)
    print("3 Sub Problem:")
    for i in range(len(PQ) - 2, -1, -1):
        print(f"{float(PQ[i])}*x^{i}", end="")
        if i - 1 != -1:
            print(" + ", end="")
    print()
    print()
    print()
    print()

    # Generating a problem and timing the three algorithms
    n = 2**4
    maxN = 2**12
    nCount = np.zeros(maxN+1)
    runtimeHS = np.zeros(maxN+1)
    rtHSBunch = []
    runtime4S = np.zeros(maxN+1)
    rt4SBunch = []
    runtime3S = np.zeros(maxN + 1)  # 3 sub problem run time
    rt3SBunch = []
    nBunch = []
    while n <= maxN:
        nCount[n] = n
        nBunch.append(n)  # Keeping track of n values used
        [P, Q] = probGen(n)
        start = time.time()
        for i in range(0, 10):
            PMHighSchool(P[i], Q[i])
        end = time.time()
        runtimeHS[n] = end - start
        rtHSBunch.append(runtimeHS[n])  # Keeping track of values computed
        start = time.time()
        for i in range(0, 10):
            PMDivConq4Sub(P[i], Q[i], n)
        end = time.time()
        runtime4S[n] = end - start
        rt4SBunch.append(runtime4S[n])  # Keeping track of values computed
        start = time.time()
        for i in range(0, 10):
            PMDivConq3Sub(P[i], Q[i], n)
        end = time.time()
        runtime3S[n] = end - start
        rt3SBunch.append(runtime3S[n])  # Keeping track of values computed

        n *= 2

    f = open("TestTiming.txt", 'w')
    f.truncate(0)
    f.write(f"P:{str(P)}")
    f.write(f"Q:{str(Q)}")
    f.close()

    slopeHS, interceptHS, slope4S, intercept4S, slope3S, intercept3S = loglogPlot3(nBunch, rtHSBunch, rt4SBunch, rt3SBunch)

    print(f"High School Equation:\nlog(runtime) = {slopeHS}*log(n) + log({interceptHS})")
    print(f"4 Sub Problem Equation:\nlog(runtime) = {slope4S}*log(n) + log({intercept4S})")
    print(f"3 Sub Problem Equation:\nlog(runtime) = {slope3S}*log(n) + log({intercept3S})")
    print()

    # Finding where 3 Sub becomes faster than HS
    # When does slopeHS*x + interceptHS = slope3S*x + intercept3S ?
    # (slopeHS - slope3S)*x = intercept3S - interceptHS
    # x = (intercept3S - interceptHS) / (slopeHS - slope3S)
    HS3Scross = abs((intercept3S - interceptHS) / (slopeHS - slope3S))
    print(f"3 Sub Problem becomes faster than HS\n at log(n) ~= {HS3Scross}")
    cross4S3S = abs((intercept3S - intercept4S) / (slope4S - slope3S))
    print(f"3 Sub Problem becomes faster than 4 Sub Problem\n at log(n) ~= {cross4S3S}")

    # Calculating difference of the intercepts compared to the high school algo
    diffHS3S = interceptHS - intercept3S
    print(f"c multiplier of 3 sub problem compared to high school = {diffHS3S}")
    diffHS4S = interceptHS - intercept4S
    print(f"c multiplier of 4 sub problem compared to high school = {diffHS4S}")


main()
