class Zombie:
    def __init__(self, zombie_name, attack_power):
        self.name = zombie_name
        self.hp = 100.0
        self.base_armor = 10.0
        self.base_damage = attack_power
        self.speed = 10.0

    def attack(self, enemy):
        damage_dealt = self.base_damage - (self.base_damage * enemy.base_armor / 100)
        enemy.take_damage(damage_dealt)

    def take_damage(self, damage_dealt):
        self.hp -= damage_dealt
        print(self.name + " is attacked..." + "\nhealth:", self.hp)
        if self.hp <= 0:
            print("HP too low no longer able to fight.")

bombur = Zombie("Bombur", 56)
athena = Zombie("Athena Goddess of wisdom", 75)

athena.attack(bombur)