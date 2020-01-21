sequence = []
subSequence = []
for i in range(0, 10):
    sequence.append(int(input("Enter the sequence of 10 numbers? ")))
for x in range(0, 3):
    subSequence.append(int(input("Enter the sequence of 3 numbers? ")))

a = 0
b = 0
verification = 0
while (a<9):
    if sequence[a] == subSequence[b]:
        b += 1
        a += 1
        if sequence[a] == subSequence[b]:
            b += 1
            a += 1
            if sequence[a] == subSequence[b]:
                print(True)
                verification = 1
                break
    a += 1

if verification == 0:
    print(False)