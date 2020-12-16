from math import sqrt
c = 3e8  #m/s
v = 1e8  #m/s
m = 0.14  #kg

gamma = 1/sqrt(1-(v**2/c**2))
p = m*v*gamma

print p
