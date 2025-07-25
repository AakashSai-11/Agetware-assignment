def convert_number_to_Indian_currency(num):
    isNegative = False
    if num<0:
        s = str(num)[1:]
        isNegative = True
    else:
        s = str(num)
    dot_index = s.find('.')
    if dot_index != -1:
        decimal_part = s[dot_index:]
        integer_part = s[:dot_index]
    else:
        decimal_part = ''
        integer_part = s

    result = []
    i = len(integer_part) - 1

    
    while i >= 0:
        result.append(integer_part[i])
        i -= 1
        if len(result) == 3 and i >= 0:
            result.append(',')
            break

    count = 0
    while i >= 0:
        result.append(integer_part[i])
        i -= 1
        count += 1
        if count == 2 and i >= 0:
            result.append(',')
            count = 0
            
    if isNegative == True:
        return '-'+''.join(result[::-1]) + decimal_part
    return ''.join(result[::-1]) + decimal_part

print(convert_number_to_Indian_currency(123456.7891))  
