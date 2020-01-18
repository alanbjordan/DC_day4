#Program will;
    #given a string 
    #translate the string in leetspeak
    #print the translated string


string = input("enter a string to convert: ").upper()

translation = ""

for i in range(len(string)):
    add_to = ""
    if string[i] == "A":
        add_to = "4"
    elif string[i] == "E":
        add_to = "5"
    elif string[i] == "G":
        add_to = "6"
    elif string[i] == "I":
        add_to = "1"
    elif string[i] == "O":
        add_to = "0"
    elif string[i] == "S":
        add_to = "5"
    elif string[i] == "T":
        add_to = "7"
    else:
        add_to = string[i]
    translation = translation + add_to
print(translation)


    