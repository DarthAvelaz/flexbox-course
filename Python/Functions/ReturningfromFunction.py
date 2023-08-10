"""
def full_name(first, last):
    return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

def greeting(name):
    print(f'Hi {name}!')


greeting(kristine)
"""

"""
def sum_two_numbers(first_number, last_number):
    return f'{first_number} {last_number}'


sum = sum_two_numbers('11', '32')

def addition(added):
    print(f'The total is {added}')

addition(sum)
"""


def greeting(first):
  def name():
    return f'{first}'

  print(f'Hi {name()}')


greeting('Kristine')