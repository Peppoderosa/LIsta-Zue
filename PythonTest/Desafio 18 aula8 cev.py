import math
a = float(input('Ângulo? '))

ac = math.radians(a)
cos = math.cos(ac)
sen = math.sin(ac)

print('O seno de {}{}{} é {}{:.3f}{} e o coseno é {}{:.3f}{}'.format('\033[7m',a,'\033[m','\033[1;32m',sen,'\033[m','\033[1;42m',cos,'\033[m'))