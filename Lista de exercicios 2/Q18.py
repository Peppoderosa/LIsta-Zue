s = str(input('Enter a word? '))
inverseS = ''

size = 0
for a in s:
    size += 1

i = 0
x = size - 1
while (i != size):
    inverseS = inverseS + s[x]
    i = i + 1
    x = x - 1

print(inverseS)

