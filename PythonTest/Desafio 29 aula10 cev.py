v = float(input('Qual a velocidade(Km/h)? '))

if v > 80:
    m = v-80
    print('Multado em R${:.2f}'.format(m*7))
else:
    print('Liberado')