def predefinedFunction(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

index = 0 
count = 0
list1 = []

while count < 100:
    if predefinedFunction(index):
        print(f"{index} egy prím")
        list1.append(f"{index}")
        count += 1
    index += 1

index2 = 0
list2 = []

for i in range(0, 100000):
    if index2 < 100:
     if predefinedFunction(i):
            print(f"{i} egy prím")
            list2.append(f"{i}")
            index2 += 1
    else:
        break


print(len(list1))
print(len(list2))