import numpy as np

# Define the matrix A
A = np.array([[1,1,0], 
              [0,1,2],
              [0,0,3]])

# Step 1: Compute eigenvalues and eigenvectors
print(np.linalg.eig(A))


'''
# Step 2: Identify the dominant eigenvalue and its corresponding eigenvector
dominant_index = np.argmax(np.abs(eigenvalues))  # Index of the dominant eigenvalue
dominant_eigenvalue = eigenvalues[dominant_index]
dominant_eigenvector = eigenvectors[:, dominant_index]

# Step 3: Normalize the dominant eigenvector
normalized_eigenvector = dominant_eigenvector / np.linalg.norm(dominant_eigenvector)

# Step 4: Compute the population distribution after 10 years
x_0 = np.array([100, 0, 0])  # Initial population
A_10 = np.linalg.matrix_power(A, 20)
x_10 = A_10 @ x_0

# Print the results
print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Normalized Dominant Eigenvector:", normalized_eigenvector)
print("Population Distribution After 10 Years:", x_10)

# Optionally compare the distributions
print("Normalized Population Distribution After 10 Years:", x_10 / np.linalg.norm(x_10))
'''