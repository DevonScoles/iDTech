import random 

#first lets create a random integer that the user will have to guess
rand_int = random.randint(1,100)

#then lets have the user guess that number and store it in a variable
user_guess = int(input("Guess any number between 1-100: "))

# #while loop for number guessing program
while True:    
    if user_guess > rand_int:
        print("Too high!")
        user_guess = int(input("Guess Again! "))
    elif user_guess < rand_int:
        print("Too Low!")
        user_guess = int(input("Guess Again! "))
    else:
        print("Correct! Wow your brain must be huge!")
        break

# ==== comment out while loop when you want to test for loop ==========

#this is the same guessing game you'll even notice I used the same code as I did in the while loop
#BUT now the player has a limited amount of guesses using the for blank in range(start,stop,step) method
for i in range(10,0,-1): # loop counts down from 10 to 0 giving the user 10 guesses and then breaks
    if int(user_guess) > rand_int:
        print("Too high!")
        user_guess = input("Guess Again! You have " + str(i) + " of guesses left. ")
    elif int(user_guess) < rand_int:
        print("Too Low!") 
        user_guess = input("Guess Again! You have " + str(i) + " of guesses left. ")
    else:
        print("Correct! Wow your brain must be huge!")
        break

    # An if statement can be added to tell the user they are out of guesses
    # How would this be done?
