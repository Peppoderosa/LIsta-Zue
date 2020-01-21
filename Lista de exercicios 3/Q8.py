def raizes (a, b, c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        x1 = ((b*(-1)) + (delta**(1/2)))/(2*a)
        x2 = ((b*(-1)) - (delta**(1/2)))/(2*a)
        return int(x1), int(x2)
    else:
        return 'Erro'

#################################################

print(raizes(1,3,2))