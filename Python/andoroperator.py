'''
username = ''
email = 'jon@snow.com'
password = 'tasdf'

if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    print('Access Permitted')
else:
    print('You Shall Not Pass!')
'''

'''
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' or password == 'thenorth':
    print('Access Permitted')
else:
    print('You Shall Not Pass!')
'''
'''
logged_in = True
standard_user = True

if logged_in and not standard_user:
    print('You can access teh Admin dashboard')
else:
    print('You can only access the standard dashboard')
'''

# 'and' operator needs both sides to be true in the expression
# 'or' needs only one side to be true in the expression
# 'and not' needs the expression to read false to run normally in the expression

def compound_conditional(number): 100

if compound_conditional == 1 or compound_conditional == 100:
        print("Success!")
else:
        print("Failure...")