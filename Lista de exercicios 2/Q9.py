a = 80000
b = 200000
years = 0

while (True):
    if a>=b:
        break
    else:
        a = a*1.03
        b = b*1.015
        years += 1

print('The population will be same in: {} years'.format(years))