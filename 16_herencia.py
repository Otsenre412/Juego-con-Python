"""
herencia de clases
"""

class vehicle:
    def __init__(self):
        self.wheels = 0
        self.name = self.__class__.__name__
        print('Constructor de', self.name)

    def move(self):
        return 'moving'

class car(vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 4

    def move(self):
        return 'moving on the road'

class plane(vehicle):
    def __init__(self):
        super().__init__()
        self.wheels = 4
    def move(self):
        return 'flaying'

VEHICLES = (vehicle(), car(), plane())

for v in VEHICLES:
    print('{} tiene {} ruedas y se mueve así: {}'.format(v.name, v.wheels, v.move()))


# herencia multiple

class A:
    def fly(self):
        print('flying')

class B:
    def run(self):
        print('running')

class C(A, B):
    def eat(self):
        print('eating')

c = C()
c.eat()
c.fly()
c.run()
