#How many coins?
#Write a program that will prompt you for how many coins you want. 
#Initially you have no coins. It will ask you if you want a coin? 
#If you type "yes", it will give you one coin, and print out the current tally. 
#If you type no, it will stop the program.

user_input = input("You have 0 coins. Do you want another? ").lower()

count = 0
while count >= 0:
    if user_input == "yes":
        count += 1
        print("You have",count,"coins.")
        user_input = input("Do you want another? ")
    elif user_input == "no":
        print("Enjoy your coins, goodbye!")
        break

