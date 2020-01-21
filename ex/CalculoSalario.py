def hour (list):
    time = float(input('Time? '))
    while (time > 0):
        list.append(time)
        time = float(input('Time? '))

def sal (listS, listH):
    for i in listH:
        if i >= 40:
            listS.append(((i-40)*30) + (i*20))
        else:
            listS.append(i*20)

list_time = []
list_sal = []

hour(list_time)
sal(list_sal, list_time)

print(list_sal)
