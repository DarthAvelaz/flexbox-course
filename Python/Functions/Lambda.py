#lambda = a function that allows user to wrap up a smaller function and pass it on to other functions
"""
full_name = lambda first, last: f'{first} {last}'


def greeting(name):
    print(f'Hi there {name}')


greeting(full_name('Tiffany', 'Hudgens'))
"""

def lambda_practice():
    first_name = lambda first: f'Hi {first}'


    def greeting(name):
        print({name})
    
    
    return greeting(first_name('Jordan'))