def madLib(): #this is a function called MadLib that takes no parameters inside the parantheses

    #print statement to say Madlib time!!! and then go down two lines
    print("MadLib time!!!\n")

    #these are variables that take ask you for words
    pluralNoun = input("Give me a plural noun: ")
    adjective = input("Now an adjective: ")
    pluralAnimal = input("How about an animal: ")
    adjAnimal = input("Now I need an adjective and animal: ")
    animal2 = input("Another animal: ")
    adjective2 = input("Okay now I need another adjective: ")
    pluralAnimal = input("Now I need a plural animal: ")
    adjective3 = input("Give me another adjective: ")
    food = input('Whats a funky food?: ')
    drink = input('Apple juice or gatorade?: ')
    adjective4 = input("Give me another adjective: ")
    pluralAnimal2 = input("Plural animal: ")
    housing = input("A fun palce to live: ")
    pluralAnimal3 = input("last but not least another plural animal: ")


    #this is the print statement inside of the function you can tell because it looks indented
    print(f'\nSo many {pluralNoun} make {adjective} pets. \nMany people like furry {pluralAnimal} or a {adjAnimal} to cuddle with. \
    \nSome people like having a {animal2} for a pet, and others prefer {adjective2} {pluralAnimal}. \nMost pets need things like {adjective3} \
    care, {food}, {drink}, exercise, and a {adjective4} place to sleep. \nSome pets like {pluralAnimal2} live in {housing},\
    but everyone can agree that {pluralAnimal3} are cute and crazy') 


madLib()