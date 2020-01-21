n1 = float(input('1ª number? '))
n2 = float(input('2ª number? '))
n3 = float(input('3ª number? '))

average = (n1+n2+n3)/3
count = 0

if n1 > average:
    count = count + 1
elif n2 > average:
    count = count + 1
elif n3 > average:
    count = count + 1

print(count)