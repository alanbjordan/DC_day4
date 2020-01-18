#Program will;
    #given a list of numbers
    #create a new list which contains every number in the given list which is positive

first_list = [1,-2,3,-4,-5,6,7,-8,9]

second_list = []

for i in range(len(first_list)):
    if first_list[i] > 0:
        second_list.append(first_list[i])
print(second_list)
