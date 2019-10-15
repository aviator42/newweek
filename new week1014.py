#looking at approximations of pi
# as  well as looking at the math module

print(22/7)
print(355/113)

import math

print(9801 / (2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math .radians(halfAngleA))
    sideS = oneHalfSideS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))

# see th loop above.  in addition to the value of pi, print the difference
#  between the values calculated by the arcimedes function and by math.pi.
#  How many sides does i take to make the two close?

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))

print(math.pi)

# it takes 360000000

# Accumulators

acc = 0
for val in range(1, 6, 1):
    acc = acc + val

print(acc)