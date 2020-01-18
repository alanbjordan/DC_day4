#Program will;
    #given a list of numbers and a single factor (also a number)
    #create a new list consisting of each of the numbers in the first list multiplied by the factor
    #print the new list

first_list = [1,2,3,4,5,6,7,8,9]
factor = 2
second_list = []

for i in range(len(first_list)):
    multi_num = first_list[i] * factor
    second_list.append(multi_num)
print(second_list)
