from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
#1
def taylor(func, start, end, degree, fixed_c):
    x = symbols('x')
    #Make an array for the x axis from start to end, dividied into 100 points
    x_axis = np.linspace(start, end, 100)
    y_axis = np.zeros(100)
    #Calculate taylor series for every point in x_axis 
    for n in range(degree):
        #nth derivitive of func at point x
        f_n_prime_of_x = lambdify(x, diff(func, x, n), 'numpy')
        #f'(x) / n!
        result = f_n_prime_of_x(fixed_c) / math.factorial(n)
        #calculate (x-c)^n
        x_minus_c_nth_power = (x_axis - fixed_c)**n
        #Add the nth iteration to the current sum
        y_axis = y_axis + (result * x_minus_c_nth_power)
    
    return y_axis


x = symbols('x')
function = (x * sin(x)**2) + cos(x)
x_axis = np.linspace(-10, 10, 100)
#2
approximation = taylor(function,-10,10,99,0)
real_function = lambdify(x, function, 'numpy')
result = real_function(x_axis)
#Plot the approximation and the actual value
plt.plot(x_axis, approximation, "o" ,color='r', label="Approximation")
plt.plot(x_axis, result , color='b',label="Real function")
plt.legend()
plt.title("Approximation vs Real value of Function")
plt.show()

#3
def taylor2(func, start, end, fixed_c, initial_degree, final_degree, degree_step ):
    #Create array of degrees we want to test
    degrees = np.arange(initial_degree,final_degree + degree_step, degree_step)
    sums = np.zeros(len(degrees))
    times = np.zeros(len(degrees))
    x = symbols('x')
    #Make an array for the x axis from start to end, dividied into 100 points
    x_axis = np.linspace(start, end, 100)
    
    #Calculate real values of function
    real_function = lambdify(x, func, 'numpy')
    real_values = real_function(x_axis)

    #Create variable to iterate through sums and time
    i = 0
    #Loop through degrees
    for degree in degrees:
        #for each m = degree compute the taylor approximation
        y_axis = np.zeros(100)
        
        #Start time
        start_time = time.perf_counter()
        #Calculate Taylor series for every point in x_axis
        for n in range(degree):
            
            #nth derivitive of func at point x
            f_n_prime_of_x = lambdify(x, diff(func, x, n), 'numpy')
            #f'(x) / n!
            result = f_n_prime_of_x(fixed_c) / math.factorial(n)
            #calculate (x-c)^n
            x_minus_c_nth_power = (x_axis - fixed_c)**n
            #Add the nth iteration to the current sum
            y_axis = y_axis + (result * x_minus_c_nth_power)
        
        #Compute difference between approximation and real value
        difference = real_values - y_axis
        difference = np.abs(difference)
        
        #Compute the sum of all differences
        sum = np.sum(difference)

        #Keep track of end time and calculate elapsed time
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        #input values into our arrays
        sums[i] = sum
        times[i] = elapsed_time
        i+=1
    
    #Create pandas dataframe
    df = pd.DataFrame({'Sums':sums, 'Elapsed Time': times})
    df.to_csv('taylor_values.csv')
    return sums

taylor2(function, -10, 10, 0, 50, 100, 10)