filer_builder = open("logger.txt", "w+")

for i in range(100):
    filer_builder.write(f"I'm on a line {i + 1}\n")

#filer_builder.write("Hey, I'm in a file!")

filer_builder.close()