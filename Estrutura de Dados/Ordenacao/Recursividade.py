def func (n):
    print(n)
    if (n>0):
        func(n-1)

def fat(n):
    if (n == 0) or (n==1):
        return 1
    elif (n>1):
        return n*fat(n-1)

def par(n):
    if n >= 0:
        n-= n%2
        print(n)
        par(n-2)

'''
def func2(n):
    print(n-1)
    func3(n-1)

def func3 (n):
    print(n-1)
    func4(n-1)

def func4 (n):
    print(n-1)
    func5(n-1)

def func5 (n):
    print(n-1)

'''
############################################################
par(45)