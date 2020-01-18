#using a while loop, print out the numbers betwween 1 and 10 inclusive 
#prompt the user for a number to start on and a number to end on

count = int(input("Enter a number to start loop: "))
break_num = int(input("Enter a number to stop loop: "))



while count <= break_num:
    print(count)
    count += 1
