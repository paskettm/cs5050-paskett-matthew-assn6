# Requirements
Do the 1/2 size sub problem algo again, but turn it into 3 sub problems instead of 2 sub problems.

## Polynomial Multiplication Problem
Multiply 2 polynomials of order n


# Design
*Begin by copying 4 sub problem code into project.*

## Polynomial Multiplication Problem (in math)
Smallest problem:
* (a + b)*(c + d) = a * c(0) + a * d(1) + b * c(1) + a * c(2) = (a * c)(0) + (a * d + b * c)(1) + (b * d)(2)
    * where (a * c) = p, (a * d + b * c) = q, (b * d) = r
      in p + qx + rx^2
    * or a = PQ_LL, b = PQ_LH, c = PQ_HL, d = PQ_HH

Turning smallest problem into 3 multiplications instead of 4 
(do addition first)
* p = (a * c), r = (b * d), q = (a + b)*(c + d) - p - r

## Empirical Study
Plot 3 algorithms' runtime on loglog graph. Measure slope and offset
(c value) of all three lines (use `numpy.polyfit`). The graphs you'll
see are according to the function **log(f(n)) = klog(n) + log(c)**
where **k** is the slope and **c** is the offset.

Answer these questions:
* Do the slopes confirm our mathematical analysis of the algorithms? AKA,
  is the slope flatter for the 3 sub problem?
* At what problem size does the n^(1.59) {3 sub} algo become faster than the other two?
* What is the **c** multiplier of the two recursive algos compared to
  the high school algo (using anti-logs to get the multiplicative factor)?
  This gives an idea of the "overhead".


# Implementation
The biggest issue with writing the code is figuring out how to turn the 
math into code for the 3 sub problem algo.


# Test Cases

I tested a small problem (given as output in the main function).

I also tested larger problems with the 3 sub against high school to 
check that they matched (given as output in the main function).