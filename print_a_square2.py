#Print a NxN square of * characters. Prompt the user for N. Example output:

input = int(input("How big is the square? "))

i = 0
j = 0
asterisk = ""

while i < input:
    while j < input:
        insert = ""
        if j < input:
            insert = "*"
        asterisk = asterisk + insert
        j += 1
    if i < input:
        print(asterisk)
        i += 1
 