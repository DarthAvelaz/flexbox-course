def some_function(collection = []):
    collection.append(1)
    print(id(collection))
    return collection


print(some_function()) #[1]


#Other part of program
print(some_function()) #[1]

#DO not do this! Setting a default value as a list draws a connection via memory. Run to observe.