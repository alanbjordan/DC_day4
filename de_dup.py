list1 = ['a','v','c','d','e','v','f','g','g','x']
# list2 = []
i = 0
list2 = []
while i < len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i += 1
print(list2)