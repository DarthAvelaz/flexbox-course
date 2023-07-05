'''
nums = list(range(1,100))

while len(nums) >0:
    print(nums.pop())
'''


'''
def guessing_game():
    while True:
        print('What is your guess?')
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            return False
        else:
            print(f'No, {guess} is not the answer, please try again\n')


guessing_game()
'''

num_list = range(1, 11)

even_numbers = []

#for num in num_list:
#    if num % 2 == 0:
#        even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)