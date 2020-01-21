def embaralha (palavra):
    palavra = palavra.lower()
    palavraList = list(palavra)
    mix = ''
    for i in palavra:
        o = int(random.randint(0, (len(palavraList)-1)))
        mix = mix + palavraList[o]
        palavraList.pop(o)

    return mix

#################################################

import random

word = 'Python'
print(embaralha(word))
