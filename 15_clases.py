"""
trabajando con clases y POO (programacion orientada a objetos)
"""

class thing:
    pass 

cosa = thing()

class fruit: 
    def __init__(self):
        print('objeto fruta inicial')

fruit = fruit()

# argumentos del constructor

class person:
    """ esta es la documentacion de la clase person """
    COUNTER = 0

    def __init__(self, name):
        self.name = name
        self.knowledge = []
        person.COUNTER += 1

    def __str__(self):
        return 'Me llamo {} y se {}'.format(self.name, self.knowledge)

    def learn(self, what):
        self.knowledge.append(what)

p1 = person('Ernesto')
p2 = person('Mary')
p3 = person('David')

p1.learn('python')
p2.learn('javascript')
p3.learn('C#')

print(p1)
print(p2)
print(p3)
print(person.COUNTER)


