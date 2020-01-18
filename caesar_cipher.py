

string = input("Enter the phrase you would like decrypted? ")

deciphered_message = ""

letter_list = "abcdefghijklmnopqrstuvwxyz"
number_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25]

for i in range(len(string)):
    add_to = " "
    for j in range(len(letter_list)):
        if string[i] == letter_list[j]:
            key_shift = j - number_list[13]  
            add_to = letter_list[key_shift]
    deciphered_message = deciphered_message + add_to    
    
print(deciphered_message) 
