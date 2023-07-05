'''
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
''' ''' player after For doesn't dictate, can be nearly anything and still work as long as it matches print variable word'''
'''for player in players:
    print(player)
'''

'''
players = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis',
}

for position, player in players.items():
    print('position', position)
    print('Player Name', player)
'''

'''
Name = 'Antonio'

for letter in Name:
    print(letter)
'''

'''
usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa',
]

for username in usernames:
    if username == 'cersei':
        print(f'Sorry, {username}, you are not allowed')
        continue
    else:
        print(f'{username} is allowed')
'''

'''        
usernames = [
    'jon',
    'tyrion',
    'theon',
    'cersei',
    'sansa',
]

for username in usernames:
    if username == 'cersei':
        print(f'{username} was found at index {usernames.index(username)}')
        break
    print(username)
'''

'''
vegetables = [
    'onion',
    'broccoli',
    'apple',
    'spinach',
]

for x in vegetables:
    if x == 'apple':
        print(f'{x} is not a vegetable')
        break
    print(vegetables)
'''