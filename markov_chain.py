import numpy as np
from sklearn.preprocessing import normalize
#1.Construct a random 5x5 matrix P and  normalize each row
matrixP = np.random.rand(5, 5)
normalMatrixP = normalize(matrixP, axis=1, norm='l1')

#2.Construct a random size-5 vectore p and normalize it
vectorp = np.random.rand(5).reshape(1,-1)
normalVectorp = normalize(vectorp, norm='l1')
normalVectorp = normalVectorp.reshape(-1)


#Apply the transition rule 50 times

#Take transpose of P
normalMatrixPTranspose = normalMatrixP.T
p50 = normalVectorp
for i in range(50):
    p50 = normalMatrixPTranspose @ p50
print(p50)
#3. Compute the eigenvector v of P^T corresponding to the eigenvalue 1, and then scale the eigenvector
eigenvalues, eigenvectors = np.linalg.eig(normalMatrixPTranspose)

#Grab eigenvector corresponding to eigenvalue 1
v = eigenvectors[:][0]

#normalize the eigenvector
sum = np.sum(v)
normalV = v / sum # This is our stationary distribution

#4.Compute the component-wise difference between p50 and v
difference = p50 - normalV
print(difference)

