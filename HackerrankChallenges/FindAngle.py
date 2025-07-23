import math
ab = int(input())
bc = int(input())
phi = math.atan2(ab, bc)    # * (180/math.pi)
print("{}{}".format(round(phi), chr(176), sep=''))
