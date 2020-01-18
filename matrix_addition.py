#Calculate the result of adding the two matrices. 
#The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.

matrix = [[2,-2],[5,3]]
matrix2 = [[3,-3],[6,5]]
combined_matrices = [[],[]]

for inner_matrices in matrix:
    a = matrix[0][0] + matrix2[0][0]
    b = matrix[0][1] + matrix2[0][1]
    c = matrix[1][0] + matrix2[1][0]
    d = matrix[1][1] + matrix2[1][1]

combined_matrices[0].append(a)
combined_matrices[0].append(b)
combined_matrices[1].append(c)
combined_matrices[1].append(d)
print("Added Matrices: ",combined_matrices)





