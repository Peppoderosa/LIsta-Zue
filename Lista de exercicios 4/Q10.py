def trans_grade(lista):
    high = max(lista, key=int)
    new_list = []
    for i in lista:
        new_list.append(i*10/high)
    print('Maior nota: {}'.format(high))
    for x in range(0, len(lista)):
        print('{} | {} | {:.1f}'.format(x+1, lista[x], new_list[x]))

#################################################

list = [3.0,4.0,5.0,6.0,3.0]
trans_grade(list)