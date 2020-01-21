positive = 0
negative = 0

while True:
    n = int(input('Enter a number? '))
    if n > 0:
        positive +=1
    elif n < 0:
        negative +=1
    elif n == 0:
        break

print('{} positives number(s)'.format(positive))
print('{} negatives number(s)'.format(negative))