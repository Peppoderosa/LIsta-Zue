a = 3
b = 5
n = 'jon'
c = {'clean':'\033[m',
     'blue':'\033[34m',
     'yellow':'\033[33m',
     'blacknWhite':'\033[7;30m'}

#print('\033[7;32mos valores são {} e {}\033[m'.format(a,b))

print('olá {}{}{}!'.format(c['blacknWhite'],n,c['clean']))