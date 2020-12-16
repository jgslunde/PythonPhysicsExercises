from math import squareroot
c = 300 000 000  # m/s
v = 100 000 000  # m/s
m = 0,14  # kg

gamma = 1/squareroot(1-(v^2/c^2))
p = m*v*gamma

print p
