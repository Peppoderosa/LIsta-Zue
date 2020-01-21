'''
from math import sqrt, floor

n = int(input('numero: '))
r = sqrt(n)

print('raiz: {:.2f}'.format(floor(r)))

--------

import random

n = random.randint(1,10)
print(n)

'''

import emoji

print(emoji.emojize('ola, :earth_americas:', use_aliases=True))