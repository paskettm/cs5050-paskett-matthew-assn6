# Analysis
The output graph is located in the main folder as `loglog.png`. Graph
from running maxN = 2**12 is located in `loglog12.png`
According to the output given to the console from running the program, 
the slopes match our mathematical analysis of the algos. The 3 sub 
problem slope has been smaller than the 4 sub problem and high school 
algorithms for the test cases used to date.

According to the slopes and intercepts calculated from the program, 
the 3 sub problem seems to become faster than the 4 sub problem algo 
almost immediately and faster than the high school algo at about 
log(n) = 6 (approx. n = 403).

The difference between the intercepts of the algorithms' polynomial fits
give us the "overhead" needed to run the 4 and 3 sub problems compared 
to the high school algorithm, which needs little overhead in comparison.
The "overhead" needed for the 3 and 4 sub problems are given in the console output.
