numbers = [9,  8, 7, 6, 10,  5, 4, 16, 3, 12, 2, 1]
numbers2 = [32, 33, 31, 36, 35]
numbersOut = []

for number in numbers:
    if len(numbersOut) == 0:
        numbersOut.append(number)
        print("First element added")
    else:
        inserted = False
        for i in range(len(numbersOut)):
            if number < numbersOut[i]:
                numbersOut.insert(i, number)
                inserted = True
                print(f"inserted {number} at {i}")
                break
        if not inserted:
            numbersOut.append(number)
            print("Appended to back")

print(numbersOut)


newList = []

for i in numbers2:
    numbers.append(i)

for number in numbers:
    if len(newList) == 0:
        newList.append(number)
        print(f"First element {number} added")
    else:
        inserted = False
        for i in range(len(newList)):
            if number < newList[i]:
                newList.insert(i, number)
                inserted = True
                print(f"inserted {number} at {i}")
                break
        if not inserted:
            newList.append(number)
            print(f"Appended {number} to back")

print(newList)