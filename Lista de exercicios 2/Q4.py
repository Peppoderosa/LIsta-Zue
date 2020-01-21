list = []
sumO = 0
sumP = 0

for i in range(0, 20):
    list.append(int(input('Enter a value? ')))

for x in list:
    if x%2==0:
        sumP += x
    else:
        sumO += x

print('The sum of pair numbers is: {}'.format(sumP))
print('The sum of odd numbers is: {}'.format(sumO))