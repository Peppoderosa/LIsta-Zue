def perfect (num):
    number = num
    lista = []

    i = 1
    while number != 1:
        number = num / i
        if number // 1 == number:
            lista.append(int(number))
        i += 1

    lista.pop(0)

    result = ''
    sum = 0
    for x in lista:
        sum += x
        result = result+str(x)
        if x != 1:
            result = result+' + '

    if sum == num:
        print('{} = {}'.format(num, result))
        return True
    else:
        return False


#################################################

print(perfect(33550336))
