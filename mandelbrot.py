import matplotlib.pyplot as plt
import numpy as np
#Function that checks how many iterations it takes for a number c to diverge
#If function returns a number n<50 then c diverges
#If function returns n = 50 then the number c converges
def mandelbrotConverge(c):
    #Initialize variables
    maxIterations = 50
    currentIteration = 0
    z = 0
    
    #While absolute value of z < 2 and currentIterations < 50
    while (abs(z) < 2) and (currentIteration < maxIterations):
        #z = z^2 + c
        z = (z**2) + c
        
        #Add one to current iterations
        currentIteration+=1

    #Return number of iterations
    return currentIteration

#Construct 1000x1000 grid
x, y = np.mgrid[-2:1:1000j , -1.5:1.5:1000j]
c = x + 1j * y

#For each point in grid, check how many iterations a point takes until it diverges
for i in range(1000):
    for k in range(1000):
       c[i][k] = mandelbrotConverge(c[i][k])

#Remove the imaginary part of each value in the grid      
c = c.real

#Plot and produce the image
plt.imshow(c,cmap='magma',vmin=1, vmax=50)
plt.axis('off')
plt.show()
