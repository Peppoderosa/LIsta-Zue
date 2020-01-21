def angulo (x, y):
    if x >= 0 and y >= 0:
        a = math.atan(y/x)
        final = a*(180/math.pi)
        return final
    else:
        return 'Error'

#################################################
import math

print(angulo(5, 1))
