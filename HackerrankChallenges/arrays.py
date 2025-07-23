from array import *
vals = array('i', [6, 9, 4, 2, 0])
print(vals.buffer_info())
vals.append(6)
print(vals)
print(vals.count(9))
vals.reverse()
print(vals)
print(vals[0])

for j in range(len(vals)):
    print(vals[j])

for e in vals:
    print(e)
