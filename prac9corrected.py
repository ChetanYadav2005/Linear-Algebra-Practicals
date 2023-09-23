import numpy as np
A = np.mat("3, -2; 1, 0")
print("A\n", A)
print('Eigenvalues', np.linalg.eigvals(A))

Eigenvalues, Eigenvectors = np.linalg.eig(A)
print("First tuple of eig", Eigenvalues)
print("second tuple of eig", Eigenvectors)

for i in range(len(Eigenvalues)):
    print("left", np.dot(A, Eigenvectors[:, i]))
    print(".........")
