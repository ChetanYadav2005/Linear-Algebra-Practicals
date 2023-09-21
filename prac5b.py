#program to find rank of a matrix
import numpy as np
Matrix = np.array([[10, 20, 10],
			[-20, -30, 10],
			[30, 50, 0]])
print("The Rank of a Matrix is: ", np.linalg.matrix_rank(Matrix))