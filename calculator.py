calculationInput = input("Input calculation: ")

calculation = calculationInput.split(" ")

calculataionLen = len(calculation)
calculataionLen = calculataionLen / 2 - 0.5 
print(calculataionLen)

count = 0
result = 0

if calculataionLen == 1:    
    while count < calculataionLen:
        count += 1
        if count % 2 != 0:
            print(calculation[(count)])
else:
    while count <= calculataionLen:
        count += 1
        if count % 2 != 0:
            print(calculation[(count)])

if calculation[(count)] == "+":
    placeHolder = int(calculation[count - 1] + int(calculation[count + 1]
    if calculation[count - 6] == "+":
        result = int(result) + int(placeHolder)
    elif calculation[count - 6] == "-":
        result = int(result) - int(placeHolder)
    elif calculation[count - 6] == "*":
        result = int(result) * int(placeHolder)
    elif calculation[count - 6] == "/":
        result = int(result) / int(placeHolder)
    else:
        result = int(result) + int(placeHolder)

if calculation[(count)] == "-":
    placeHolder = (calculation[count - 1]) - (calculation[count + 1])
    if calculation[count - 6] == "+":
        result = int(result) + int(placeHolder)
    elif calculation[count - 6] == "-":
        result = int(result) - int(placeHolder)
    elif calculation[count - 6] == "*":
        result = int(result) * int(placeHolder)
    elif calculation[count - 6] == "/":
        result = int(result) / int(placeHolder)
    else:
        result = int(result) + int(placeHolder)

if calculation[(count)] == "*":
    placeHolder = (calculation[count - 1]) * (calculation[count + 1])
    if calculation[count - 6] == "+":
        result = int(result) + int(placeHolder)
    elif calculation[count - 6] == "-":
        result = int(result) - int(placeHolder)
    elif calculation[count - 6] == "*":
        result = int(result) * int(placeHolder)
    elif calculation[count - 6] == "/":
        result = int(result) / int(placeHolder)
    else:
        result = int(result) + int(placeHolder)#

if calculation[(count)] == "/":
    placeHolder = (calculation[count - 1] / (calculation[count + 1])
    if calculation[count - 6] == "+":
        result = int(result) + int(placeHolder)
    elif calculation[count - 6] == "-":
        result = int(result) - int(placeHolder)
    elif calculation[count - 6] == "*":
        result = int(result) * int(placeHolder)
    elif calculation[count - 6] == "/":
        result = int(result) / int(placeHolder)
    else:
        result = int(result) + int(placeHolder)
