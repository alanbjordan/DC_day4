i = 1
j = 1
k = 0


num = '1234567890'

while k < 10:
    k += 1
    if i > 1:
        print("...............")
    for m in num:
       result = j * i
       print([i],"x",[j],"=",result)
       j += 1
    j = 1
    i += 1 
    