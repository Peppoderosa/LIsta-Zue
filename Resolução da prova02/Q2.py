lista = input("Enter? ")
soma = 0
for i in range(0,6):
    c = lista[i]
    if ((ord(c) >= 48) and (ord(c) <= 57)):
        n = ord(c) - 48
    elif ((ord(c) >= 97) and (ord(c) <= 122)):
        n = ord(c) - 96
    soma += n

print(soma)