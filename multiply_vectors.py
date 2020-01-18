#Program will;
    #given two list of numbers of the same length
    #create a new list by multiplying the pairs of number in corresponding positions in the two list

list1 = [1,2,3,4,5,6,7,8,9]
list2 = [9,8,7,6,5,4,3,2,1]
new_list = []

for i in range(len(list1)):
    x = list1[i] 
    y = list2[i]
    xy_product = x * y
    new_list.append(xy_product) 
print(new_list)
