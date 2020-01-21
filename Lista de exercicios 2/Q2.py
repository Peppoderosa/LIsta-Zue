height = []
age = []
for n in range(0,10):
    height.append(float(input('Enter a height? ')))
    age.append(int(input('Enter an age? ')))

sum = 0
for i in age:
    sum = sum + i

highest = 0
for a in height:
    if a > highest:
        highest = a

lowest = height[0]
for x in height:
    if x < lowest:
        lowest = x

print('Average between ages is: {:.2f}'.format(sum/len(age)))
print('The highest height is: {:.2f} '.format(highest))
print('The lowest height is: {:.2f} '.format(lowest))