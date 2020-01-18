#Program will;
    #given a word as a string
    #print the result of extending any long vowels to the length of 5

string = input("Enter a phrase: ").upper()

long_vowels = ""

for i in range(len(string)):
    add_to = ""
    if string[i] == "A":
        add_to = "AAAAA"
    elif string[i] == "E":
        add_to = "EEEEE"
    elif string[i] == "I":
        add_to = "IIIII"
    elif string[i] == "O":
        add_to = "OOOOO"
    elif string[i] == "U":
        add_to = "UUUUU"
    else: 
        add_to = string[i]
    long_vowels = long_vowels + add_to
print(long_vowels.title())




