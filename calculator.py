calculationInput = input("Input calculation: ")

calculation = calculationInput.split(" ")

calculataionLen = len(calculation)
calculataionLen = calculataionLen / 2 + 0.5
print(calculataionLen)

count = 0

while count <= calculataionLen:
    count += 1
    if count % 2 != 0:
        print(calculation[(count)])
