def comp (list1, list2):
    c = 0
    if list1 == list2:
        return True
    else:
        for i in list1:
            for x in list2:
                if i == x:
                    c += 1

    if len(list1) > len(list2) and c == len(list2):
       return True
    elif len(list2) > len(list1) and c == len(list1):
       return True
    else:
        return False

#################################################

listaA = [1,2,3,5]
listaB = [1,2,3,5]

print(comp(listaA, listaB))