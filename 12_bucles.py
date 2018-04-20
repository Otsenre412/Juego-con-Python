
def print_all(*args):
    for n in args:
        print(n)

print_all('pera', 'manzanas', 'limón')

def print_all_with_position(*args):
    for count, thing in enumerate(args):
        print('{}. {}'.format(count, thing))

print_all_with_position('pera', 'manzanas', 'limón')

count = 0
while True: 
    count += 1
    print(count)
    if(count == 100):
        break

count = 200
while count < 250:
    count += 1
    print(count)

def show_keywords_arguments(**kwargs):
    for name, value in kwargs.items():
        print('{}: {}'. format(name, value))

show_keywords_arguments(name='ernesto', age=25)