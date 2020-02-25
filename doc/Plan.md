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

Turning smallest problem into 3 multiplications instead of 4 
(do addition first)
* p = (a * c), r = (b * d), q = (a + b)*(c + d) - p - r

