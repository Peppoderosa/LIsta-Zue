def super():
    n = 1

    while n > 0:
        n = int(input('Number? '))
        alg = str(n)
        if primo(n):
            p = 1
            for i in range(0, len(alg)):
                if primo(int(alg[i])):
                    p += 1
            if p == len(alg)+1:
                print('{} é super'.format(n))
            else:
                print('{} é primo'.format(n))
        else:
            print('{} não é nada'.format(n))

#################################################

def primo(n):
    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

#################################################

super()