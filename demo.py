#SPECIAL VARIABLE __name__
#import mycode

#print("It's time to calculate",__name__)


#def add():
#    print('result 1: ')

#def sub():
#    print('result 2: ')

#def flo():
#    add()
#    sub()

#if __name__ == '__main__':
#    flo()



#OBJECT AND CLASSES

#class Monster:
#    health = 65
#    energy = 55

#    def attack(self,amount):
#        print('The monster has attacked')
#        monster.health -= 10
#        print(monster.health)
#        print(f'{amount} damage was dealt')

#    def move(self,speed):
#        print('The monster has moved' )
#        print(f'It has a speed of {speed}')

#monster = Monster()
#monster.attack(35)
#monster.move('77km/hr')


#2
#class Monster:

#    def __init__(self,health,energy):
#        self.health = health
#        self.energy = energy

#    def __len__(self):
#        return self.energy

#    def __abs__(self):
#        return self.health

#    def __call__(self):
#        print('The monster was called')

#    def __add__(self, other):
#        return self.health + other

#    def __str__(self):
#        return 'A monster was killed accidently'

#    def attack(self,amount):
#        print('The monster has attacked')
#        print(f'{amount} damage was done')
#        monster1.energy += 10
#        print(f'Energy update : {monster1.energy}')

#    def move(self,speed):
#        print('The monster has moved')
#        print(f'It has a speed of {speed}')

#monster1 = Monster(67,87)
#monster2 = Monster(34,45)

#print(monster1.health)
#print(monster2.health)

#print(len(monster2))
#print(abs(monster2))
#print(dir(monster1))
#print(monster2 + 50)
#print(str(monster1))


#3
#def add(a,b):
#    return a + b

#class Test:

#    def __init__(self,add_func):
#        self.add_func = add_func

#test = Test(add_func = add)
#print(test.add_func(1,2))


#4
#class Monster:
#    def __init__(self,func):
#        self.func = func

#class Attack:

#    def bite(self):
#        print("The monster's bite")

#    def strike(self):
#        print("The monster's strike")

#    def slash(self):
#        print("The Monster's slash")

#    def kick(self):
#        print("The monster's kick")

#attack = Attack()
#monster = Monster(func = attack.bite)
#monster.func()



#SCOPE
#1
#def update_energy(amount):
#    monster.energy += amount

#class Monster:
#    def __init__(self,health,energy):
#        self.health = health
#        self.energy = energy

#monster = Monster(health = 89, energy = 77)
#update_energy(20)
#print(monster.energy)


#2
#class Monster:
#    def __init__(self,health,energy):
#        self.health = health
#        self.energy = energy

#    def update_energy(self,amount):
#       self.energy += amount

#monster = Monster(health = 89, energy = 77)
#monster.update_energy(20)
#print(monster.energy)


#3
#class Monster:
#    def __init__(self,health,energy):
#        self.health = self.set_health(health)
#        self.energy = energy

#    def update_energy(self,amount):
#       self.energy += amount

#    def set_health(self,health):
#        new_health = health * 2
#        return new_health


#monster = Monster(health = 89, energy = 77)
#monster.update_energy(20)
#print(monster.energy)
#print(monster.health)


#4
#class Monster:
#    def __init__(self,health,energy):
#        self.health = health
#        self.energy = energy

#    def get_damage(self,amount):
#        self.health -= amount

#    def update_energy(self,amount):
#       self.energy += amount

#class Hero:
#    def __init__(self,damage,monster):
#        self.damage = damage
#        self.monster = monster

#    def attack(self):
#        self.monster.get_damage(self.damage)

#monster = Monster(100,90)
#hero = Hero(damage = 10, monster = monster)
#print(f"The monster's start health: {monster.health}")
#hero.attack()
#print(f"The hero attacked and reduce the monster's health to {monster.health}")



# INHERITANCE
#1
#class Monster:
#    health = 65
#    energy = 55

#    def attack(self,amount):
#        print('The monster has attacked')
#        monster.health -= amount
#        print(monster.health)
#        print(f'{amount} damage was dealt')

#    def move(self,speed):
#        print('The monster has moved' )
#        print(f'It has a speed of {speed}')

#class Shark(Monster):
#    def __init__(self,speed):
#        self.speed = speed

#monster = Monster()
#shark = Shark(speed = '120km/hr')
#print(f"The speed of the shark: {shark.speed}")
#shark.attack(15)
#print(f"The shark inherited the monster's health of : {shark.health}")



#2
#class Monster:
#    def __init__(self,health,energy):
#        self.health = health
#        self.energy = energy

#    def attack(self,amount):
#        print('The monster has attacked')
#        monster.health -= amount
#        print(monster.health)
 #       print(f'{amount} damage was dealt')

 #   def move(self,speed):
 #       print('The monster has moved' )
 #       print(f'It has a speed of {speed}')

#class Shark(Monster):
#    def __init__(self,speed,health,energy):
#        Monster.__init__(self,health,energy)  #calling the monster __init__  method in th shark
        #OR
#        super().__init__(health,energy)
#        super().move(10)

#        self.speed = speed

#    def bite(self):
#        print('The shark has bitten')

#overwritting the move function of the monster
#    def move(self):
 #       print('The shark has moved')
 #       print(f"The speed of the shark is {self.speed}")

#shark = Shark(speed = '120km/hr',health = 89, energy = 90)
#shark.move()
#print(f"The shark's inherited the parent__init__ method, health: {shark.health}")
#print(f"The shark's inherited the parent__init__ method , energy: {shark.energy}")



#3
#class Monster:
#    def __init__(self, health, energy):
#        self.health = health
#        self.energy = energy

#    def attack(self, amount):
#        print('The monster has attacked')
#        monster.health -= amount
#        print(monster.health)
#        print(f'{amount} damage was dealt')

#    def move(self, speed):
#        print('The monster has moved')
 #       print(f'It has a speed of {speed}')



#4
#class Shark(Monster):
#    def __init__(self, speed, health, energy):
#        Monster.__init__(self, health, energy)  # calling the monster __init__  method in th shark
        # OR
#        super().__init__(health, energy)
#        super().move(10)

#        self.speed = speed

#    def bite(self):
#        print('The shark has bitten')

    # overwritting the move function of the monster
#    def move(self):
#        print('The shark has moved')
#        print(f"The speed of the shark is {self.speed}")

#class Scorpion(Monster):
#    def __init__(self,poison_damage,scorpion_health,scorpion_energy):
#        super().__init__(health = scorpion_health, energy = scorpion_energy)
#        self.poison_damage = poison_damage

#    def attack(self):
#        print('The scorpion has attacked')
#        print(f'It has dealth {self.poison_damage} poison damage')

#scorpion = Scorpion(poison_damage=15,scorpion_health = 89, scorpion_energy = 77)
#scorpion.attack()
#print(scorpion.health)




#5

#class Monster:
#    '''A MONSTER THAT SOME ATTRIBUTES'''   #__doc__
#    def __init__(self, health, energy,**kwargs):
#        print(kwargs)
#        self.health = health
#        self.energy = energy
#        super().__init__(**kwargs)

        #private attribute
#        self._id = 5 # means should not be changed

#    def attack(self, amount):
#        print('The monster has attacked')
#        monster.health -= amount
#        print(monster.health)
#        print(f'{amount} damage was dealt')

#    def move(self, speed):
#        print('The monster has moved')
#        print(f'It has a speed of {speed}')

#class Fish:
#    def __init__(self,speed,has_scales):
#        self.speed = speed
#        self.has_scales = has_scales
#        super().__init__() #if there's any other class to be inherited

#    def swim(self):
#        print(f'The fish is swimming at a speed of {self.speed}')

#class  Shark(Monster,Fish):
#    def __init__(self,bite_strength,health,energy,speed,has_scales):
#        super().__init__(health = health,energy = energy, speed = speed, has_scales = has_scales)

#monster = Monster(90,80)
#shark = Shark(bite_strength = 15,
#              health = 89,
#              energy = 76,
#              speed= 67,
#              has_scales = False)

#print(shark.has_scales)
#print(shark.speed)
#shark.attack(10)

#print(monster._id)

#hasattr
#print(hasattr(monster,'health'))

#if hasattr(monster,'health'):
#    print(f'The monster has {monster.health} health')


#setattr
#setattr(monster,'weapon', 'sword')
#print(monster.weapon)

#new_attribute = (['weapon','axe'],['armor','shield'],['potion','mana'])
#for attr,value in new_attribute:
#    setattr(monster,attr,value)
#print(vars(monster))

#doc
#print(monster.__doc__)
