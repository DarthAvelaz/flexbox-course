def greeting(*args): #needs asterisk in front of args
    print('Hi ' + ' '.join(args)) #does not need asterisk in front of args. Only in the declaration.


greeting('Tiffany', 'Kristine')
greeting('Kristine', 'M', 'Hudgens')

#output is a tuple data structure