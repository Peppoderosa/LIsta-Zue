gain = float(input('How much you gain per hour? '))
hours = float(input('How much you work in one month? '))

salary = gain*hours





print('You should gain {} in end of the month.'.format(salary))
ir = salary*0.11
print('But you need pay 11% to IR, so: {}'.format(ir))
salary = salary-ir
inss = salary*0.08
print('And you need pay 8% to INSS, so: {}'.format(inss))
salary = salary-inss
syndicate = salary*0.05
print('And... yes, you need pay 5% to Syndicate, so: {}'.format(syndicate))
salary = salary-syndicate
print('Now, you will realy gain: {}'.format(salary))