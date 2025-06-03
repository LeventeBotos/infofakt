kiadasFile = open("/Users/leventebotos/infofakt/konyvkiadas/kiadas.txt", "r")
kiadasArray = kiadasFile.readlines()
kiadas = []
for i in kiadasArray:
    i = i.strip()
    i = i.split(";")
    kiadas.append(i)
kiadasFile.close()

kiadas2File = open("/Users/leventebotos/infofakt/konyvkiadas/kiadas2.txt", "r")
kiadas2Array = kiadas2File.readlines()
kiadas2 = []
for i in kiadas2Array:
    i = i.strip()
    i = i.split(";")
    kiadas2.append(i)
kiadas2File.close()

# print(kiadas)
# print(kiadas2)

print("2. feladat:")
szerzoNev = input("Szerző: ")
szerzoNev = szerzoNev.lower()
szerzoNev = szerzoNev.strip()
szerzoNevHanyszor = 0
for i in kiadas: 
    nev= i[3].split(":")[0].lower()
    nevArray = nev.split(",")
    if len(nevArray) > 1:
        nevArr = nev.split(",")
        nev = nevArr[1].strip() + " " + nevArr[0].strip()

    if nev == szerzoNev:
        szerzoNevHanyszor += 1
     
if (szerzoNevHanyszor > 0):
    print(szerzoNevHanyszor + " könyvkiadás")
else:
    print("Nem adtak ki")



print("3. feladat:")
max = 0
howManyMax = 0
for i in kiadas:
    if int(i[4]) > max:
        max = int(i[4])
        howManyMax = 1
    elif int(i[4]) == max:
        howManyMax += 1

print("A legnagyobb példányszám: " + str(max) + ", előfordult " + str(howManyMax) + " alkalommal.")


print("4. feladat:")
for i in kiadas:
    if int(i[4]) == 40000:
        print(f"{i[0]}/{i[1]}. {i[3]}")

print("5. feladat:")


print("6. feladat:")
twice = []
multiples = []
for i in kiadas:
    for j in kiadas:
        if i[3] == j[3]:
            if i[3] in twice:
                multiples.append(i[3])
            else:
                twice.append(i[3])

print("Legalább kétszer, nagyobb példányszámban újra kiadott könyvek:")
for i in multiples:
    print(f"{i}\n")