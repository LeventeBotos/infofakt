out= open("output.txt", "w")
out.write("Hiya!")
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