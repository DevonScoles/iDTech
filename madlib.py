#print statement to say Madlib time!!! and then go down two lines
print("MadLib time!!!\n")

#these are variables that ask you for words
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

#multiple print statements for each sentence such as...
print('\n So many ' + pluralNoun + ' make ' + adjective + ' pets.')
print('Many people like furry ' + pluralAnimal + ' or a ' + adjAnimal + ' to cuddle with.')
print('Some people like having a ' + animal2 + ' for a pet, and others prefer ' + adjective2 + pluralAnimal + '.')
print('Most pets need things like ' + adjective3 + 'care, ' + food + drink + ' exercise, and a ' + adjective4 + 'place to sleep.')
print('Some pets like ' + pluralAnimal2 + 'live in ' + housing + ', but everyone can agree that' + pluralAnimal3 + 'are cute and crazy.')

# [MORE ADVANCED] or only one print statement that utilizes f for format but needs \n more often
print(f'\nSo many {pluralNoun} make {adjective} pets. \nMany people like furry {pluralAnimal} or a {adjAnimal} to cuddle with. \
\nSome people like having a {animal2} for a pet, and others prefer {adjective2} {pluralAnimal}. \nMost pets need things like {adjective3} \
care, {food}, {drink}, exercise, and a {adjective4} place to sleep. \nSome pets like {pluralAnimal2} live in {housing},\
but everyone can agree that {pluralAnimal3} are cute and crazy.') 
