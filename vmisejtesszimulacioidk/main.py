def replaceMiddle(inp, data):
    for item in data:
        if len(item) > 1 and item[0] == inp:  
            return item[1]
    return None 

with open('/Users/leventebotos/infofakt/vmisejtesszimulacioidk/sejt.txt', 'r') as file:
    file1 = [line.strip().split() for line in file if line.strip()]

initArray = [char for part in file1[-1] for char in part]  
doneArray = [initArray[0]]

file1.pop()

print("file1:", file1)
print("initArray:", initArray)
print("doneArray:", doneArray)

cycleNumber = int(input("Hány ciklusban fusson le? \n"))

i = 1
while i < cycleNumber and i + 1 < len(initArray): 
    temp = initArray[i-1] + initArray[i] + initArray[i+1]
    tempp = replaceMiddle(temp, file1)

    if tempp is not None:  
        doneArray.append(tempp)

    i += 1  

print(doneArray)
