class Zombie:
    def __init__(self, name, age, size):
        self.name = name
        self.age = str(age)
        self.size = size

    def zombie_intro(self):
        print("aaaaaaaaaaaaaAAAAAAAAAAghhhh my name is " + self.name + ". I'm a zombie who can talk. I'm over " + self.age 
            + " years old. I'm also a " + self.size +" zombie.")

z1 = Zombie("Bombur", 453 , "giant")
z2 = Zombie("Athena Goddess of wisdom", 5246, "human-sized")

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting = True
 
    def stand_up(self):
        self.isSitting = False

    
p1 = Person("Metis goddess of council", "aggressive", False)
p2 = Person("Thorin Oakenshield", "greedy", True)

p1.zombie_owned = z2
p2.zombie_owned = z1

p1.zombie_owned.zombie_intro()
p2.zombie_owned.zombie_intro()