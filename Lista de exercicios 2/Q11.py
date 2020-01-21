iYear = int(input('Initial year? '))
fYear = int(input('Final year? '))

for i in range(iYear, (fYear+1)):
    if i % 4 == 0:
        if i % 100 != 0 or i % 400 == 0:
            print(i)

