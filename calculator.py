import re

calculation_input = input('Input calc :')
result = re.split('(\W)', calculation_input)

result_length = len(result)

for count in range(result_length):
    if result[count] == '*':
        multiply_result = int(result[count-1]) * int(result[count+1])
        result[count] = multiply_result
        del result[count-1]
        del result[count]
    if result[count] == '/':
        divide_result = int(result[count-1]) / int(result[count+1])
        result[count] = divide_result
        del result[count-1]
        del result[count]
    print(count)

result_length = len(result)

for count in range(result_length):
    if result[count] == '+':
        multiply_result = int(result[count-1]) + int(result[count+1])
        result[count] = multiply_result
        del result[count-1]
        del result[count]
    if result[count] == '-':
        divide_result = int(result[count-1]) - int(result[count+1])
        result[count] = divide_result
        del result[count-1]
        del result[count]
    print(count)
