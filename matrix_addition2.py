# #Calculate the result of adding the two matrices. 
# #The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices.

mx = [[2,-2],[5,3]]
mx2 = [[3,-3],[6,5]]

if len(mx) == len(mx2):
    z = []
    x = 0
    y = 0
    while x < len(mx):
        v = []
        while y < len(mx[x]):
            v.append(mx[x][y] + mx2[x][y])   
            y += 1     
        x += 1
        y = 0
        z.append(v)
print(z)

