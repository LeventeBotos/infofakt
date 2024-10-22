out= open("output.txt", "w")

out.write("Hiya!\n")


a,b = 2.4, 2.6
out.write(str(a) + " " + str(b))

out.close()

out = open("output.txt", "r")

print(out.read())

out.close()

inp = open("input.txt", "r")
# print(inp.read())
## xor
st = inp.readline()
st = st.replace("\n", " ")
print(st)

print(inp.readline())
print(inp.readline())

inp.close()