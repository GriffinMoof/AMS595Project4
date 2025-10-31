# AMS595Project4
Mandelbrot Set: For the mandelbrot set I used a similar method to the last project. I created a function mandelbrotConvergence() that would return the number of iterations it would take for a point c to diverge. If the function returns 50, the point c converges which means c is an element of the mandelbrot set. I then used numpy to create a 1000x1000 plot of the mandelbrot set and checked if every point converged by using the function I created. 

Markov Chain: First I created a random 5x5 normalized matrix using numpy and sklearns normalize function. When attempting to normalize a vector or array using the tools numpy provides, I could not seem to get the entries in each row to sum to 1. They would always be off by a few decimal places. I was not able to successfully normalize the eigenvector due to the vector having complex values and sklearns normalize function not supporting complex values. As an attempted solution I found out that numpys eig function automatically normalizes the values, so I just divided each entry in the eigenvector by the entries sum. However the matrix P and vector p were both successfully normalized. In the end I was not able to get the difference to less than 10^-5.


Taylor Series: The function taylor() approximates a given function starting at c across 100 points in the given interval. Using numpy and sympy, I was able to calculate all 100 points taylor series at the same time. It would then return the set of approximations as a numpy array. 

I then created a function taylor2() that approximates the given function for different values of m and tracks the amount of time each calculation takes along with how precise the calculation is. This data is stored in a pandas data frame and then downloaded as a csv file. 
