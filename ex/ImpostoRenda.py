def impRen (salary):
    if salary < 937:
        print('This is impossible!')
    elif salary <= 1500:
        print('You are free!')
    else:
        print('You will pay: {}'.format(salary*0.27))

def preList (lista, x):
    return (lista.append(x))

group1 = []
group2 = []

while True:
    s = float(input('Enter a salary? '))
    if s < 937:
        break
    else:
        impRen(s)
        preList(group1, s)

print(group1)

