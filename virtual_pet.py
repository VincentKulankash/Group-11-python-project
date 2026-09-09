class Pet: 
    def __init__(self, name, animal_type, hunger=5, energy=5):
        self.name = name
        self.animal_type = animal_type
        self.hunger = hunger
        self.energy = energy

    def feed(self, amount):
        self.hunger -= amount
        if self.hunger < 0:
            self.hunger = 0
        print(f"{self.name} has been fed. Hunger level is now {self.hunger}")

    def play(self):
        if self.energy > 0:
            self.energy -= 1
            self.hunger += 1
            print (f"{self.name} Played and is now more hungry. Hunger Level: {self.hunger}, Energy Level: {self.energy}")

    def status(self):
        print(f"""___Milo ___
        Type: {self.animal_type}
        Hunger: {self.hunger}
        Energy: {self.energy}
        Milo enjoyed the food:""")

  
pet1 =Pet("Milo", 'Dog')
pet1.feed(3)
pet1.play()
      