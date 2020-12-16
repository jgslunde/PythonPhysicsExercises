import sys
from math import sqrt

c = 3e8

# Exercise a) input:
# m = float(raw_input("mass of object: "))
# v = float(raw_input("velocity of object: "))

try:
    m = float(sys.argv[1])
    v = float(sys.argv[2])
except ValueError:
    print "Input cannot be converted to float."
    sys.exit()
except IndexError:
    print "Too few command line arguments."
    sys.exit()

if m < 0:
    raise ValueError, "Mass cannot be negative."
if v > 3e8:
    raise ValueError, "Speed cannot be greater than c."

if v > 1e8:  # Classical case corresponds to gamma = 1.
    gamma = 1/sqrt(1-v**2/c**2)
else:
    gamma = 1

p = m*v*gamma
print "Momentum of object is %g kgm/s" % p
