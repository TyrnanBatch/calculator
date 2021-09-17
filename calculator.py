calculation_input = '100*3+10/2'

def calculator(calculation_input):
    import re
    result = re.split('(\W)', calculation_input)

    result_length = len(result)

    count = 0
    for char in range(result_length):
        if result[count] == '*':
            multiply_result = int(result[count-1]) * int(result[count+1])
            result[count] = multiply_result
            del result[count-1]
            del result[count]
            count = 0
        if result[count] == '/':
            divide_result = int(result[count-1]) / int(result[count+1])
            result[count] = divide_result
            del result[count-1]
            del result[count]
            count = 0
        if len(result) == 1:
            return result[0]
        count += 1

    count = 0
    for char in range(result_length):
        if result[count] == '+':
            plus_result = int(result[count-1]) + int(result[count+1])
            result[count] = plus_result
            del result[count-1]
            del result[count]
            count = 0
        if result[count] == '-':
            minus_result = int(result[count-1]) - int(result[count+1])
            result[count] = minus_result
            del result[count-1]
            del result[count]
            count = 0
        if len(result) == 1:
            return result[0]
        count += 1

print(calculator(calculation_input))
