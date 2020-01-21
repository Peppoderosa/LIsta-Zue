def sum_den (n):
    s = 0
    for i in range(1,  n+1):
        s = s + (1/i)

    return s

#################################################

print(sum_den(5))