count0 = 0
count26 = 0
count51 = 0
count76 = 0

while (True):
    n = int(input('A number? '))
    if n<0:
        break
    elif n >= 0 and n <= 25:
        count0 += 1
    elif n >= 26 and n <= 50:
        count26 += 1
    elif n >= 51 and n <= 75:
        count51 += 1
    elif n >= 76 and n <= 100:
        count76 += 1

print('between 0 and 25:  {}'.format(count0))
print('between 26 and 50:  {}'.format(count26))
print('between 51 and 75:  {}'.format(count51))
print('between 76 and 100:  {}'.format(count76))