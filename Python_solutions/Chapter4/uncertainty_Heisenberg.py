import sys
from math import pi

# b)
def test_uncertainty(x,p):
    h = 6.626e-34
    assert x*p >= h/(4*pi), \
    "Deltax and deltap does not hold with the uncartainty principle"

# a)
try:
    deltax = float(sys.argv[1])
    deltap = float(sys.argv[2])
    test_uncertainty(deltax,deltap)
except IndexError:
    print "Not enough input arguments"
except ValueError:
    print "Value cannot be converted to float"
