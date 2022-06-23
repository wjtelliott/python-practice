from unicodedata import name


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    get_name = lambda self: self.name

class Zoo:
    def __init__(self, name = 'Local Zoo') -> None:
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} now has a new {animal}")
    
    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} now has many new animals")

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"{customer} has entered {self.name}")
    
    def remove_customer(self, customer):
        self.customers.remove(customer)
        print(f"{customer} has left {self.name}")

    def visit_animals(self):
        for ani in self.animals:
            print(f"Visiting the {ani.get_name()}")
            ani.make_noise()
            ani.eat_food()


class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.noise = "Every animal has a noise"
        self.food = "All creatures need sustenance"
    get_name = lambda self: self.name
    make_noise = lambda self: print(self.noise)
    eat_food = lambda self: print(self.food)


class Customer(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.has_ticket = False
        self.visiting = False

    def buy_ticket(self, child = False):
        self.has_ticket = True
        print("{name} has bought a {ticket}"
            .format(name = self.name, ticket = 'children\'s ticket' if child else 'ticket'))

    def enter_zoo(self, zoo):
        if not self.has_ticket: return
        else: self.has_ticket = False
        zoo.add_customer(self.name)
        self.visiting = True
    
    def exit_zoo(self, zoo):
        if not self.visiting: return
        self.visiting = False
        zoo.remove_customer(self.name)

class Fish(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.noise = f"{name} goes splash splash!"
        self.food = f"{name} eats smaller fish!"

class Bird(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.noise = f"{name} goes caw caw!"
        self.food = f"{name} eats worm."

class Chimp(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.noise = f"{name} goes oo-oo-ahh-ahh"
        self.food = f"{name} eats a banana."

# Use these classes....
nycZoo = Zoo('NYC Zoo')

salmon = Fish('salmon')
robin = Bird('robin')
bonobo = Chimp('bonobo')
nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer('Alice', 25)
bob = Customer('Robert', 20)
charlie = Customer('Charlie', 10)
dave = Customer('David', 30)

for c in [alice, bob, charlie, dave]:
    c.buy_ticket(not 'a' in c.name.lower())
    c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)
