file = open('/Users/leventebotos/infofakt/data/hello.txt', 'r')

content = file.read()

print(content)

file2 = open('./out.txt', "w")

file2.write(content)

file2.close()