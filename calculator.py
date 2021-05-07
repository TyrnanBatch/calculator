calculationInputO = input("Input calculation: ")

calculationInput = "+ " + calculationInputO

calculation = calculationInput.split(" ")

calculataionLen = len(calculation)
calculataionLen = calculataionLen

count = 0
result = 0

while count <= calculataionLen:
    if calculation[count - 1] == "+" and count % 2 != 0:
        result = int(result) + int(calculation[count])

    if calculation[count - 1] == "-" and count % 2 != 0:
        result = int(result) - int(calculation[count])

    if calculation[count - 1] == "*" and count % 2 != 0:
        result = int(result) * int(calculation[count])

    if calculation[count - 1] == "/" and count % 2 != 0:
        result = int(result) / int(calculation[count])
    count += 1

print(result)
