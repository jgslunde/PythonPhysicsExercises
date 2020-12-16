c = 3e8
m = 1200

# __Exercise a__
print "\n%12s%16s" % ("Vel.(m/s)", "Mom.(kgm/s)")
for i in range(0,10):
    v = 0.1*i*c
    p = m*v
    print "%11.4g%16.4g" % (v,p)

# __Exercise b__
from math import sqrt
print "\n%12s%20s%20s" % ("Vel.(c)", "Clas.Mom.(kgm/s)", "Rel.Mom.(kgm/s)")
for i in range(0,10):
    v = 0.1*i*c
    p_classic = m*v
    gamma = 1/sqrt(1-(v**2/c**2))
    p_rel = m*v*gamma
    print "%10gc%20.4g%20.4g" % (0.1*i, p_classic, p_rel)
