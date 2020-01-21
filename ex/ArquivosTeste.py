'''
arq = open("test.txt")
#arq.write("Oi")
arq.close()
arq = open("test.txt")
x = arq.read(-1)
print(x)


f = open('test.txt', 'r+')
linha1 = f.readline()
linha2 = f.readline()
f.write('\nOla Ufal')
linha3 = f.readline()
f.close()
print(linha1)
print(linha2)
print(linha3)
'''

lista = ['Ola mundo\n', 'Ola Python\n', 'Ola UFAL']
f = open('test.txt', 'w')
f.writelines(lista)
f = open('test.txt', 'r')
cont = f.readlines()
print(cont)
