value = int(input('How many you wish drop? '))


m100 = value//100
value = value - (m100*100)

m50 = value//50
value = value - (m50*50)

m20 = value//20
value = value - (m20*20)

m10 = value//10
value = value - (m10*10)

m5 = value//5
value = value - (m5*5)

m1 = value//1
value = value - (m1*1)

print ("notas de 100: {}".format( m100))
print ("notas de 50: {}".format( m50))
print ("notas de 20: {}".format( m20))
print ("notas de 10: {}".format( m10))
print ("notas de 5: {}".format( m5))
print ("notas de 1: {}".format( m1))

