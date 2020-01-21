def to_one(n):
    count = 0
    while n != 1:
        count += 1
        if n%2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

    return count


#################################################

print(to_one(5))