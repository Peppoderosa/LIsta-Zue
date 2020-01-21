vote = 0
ana = 0
bruno = 0
carlos = 0
white = 0
invalid = 0

while (True):
    print('--- Elections ---')
    print('0 - to vote white')
    print('1 - to vote in Ana')
    print('2 - to vote in Bruno')
    print('3 - to vote in Carlos')
    print('9 - to see results')
    vote = int(input('Enter: '))
    if vote == 0:
        white +=1
    elif vote == 1:
        ana += 1
    elif vote == 2:
        bruno += 1
    elif vote == 3:
        carlos += 1
    elif vote == 9:
        break
    else:
        invalid += 1

print('--- Results ---')
print('Ana had {} votes'.format(ana))
print('Bruno had {} votes'.format(bruno))
print('Carlos had {} votes'.format(carlos))
print('There ware {} whites votes'.format(white))
print(('There ware {} null votes'.format(invalid)))
