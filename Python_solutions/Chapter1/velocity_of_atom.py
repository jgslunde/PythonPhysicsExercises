from math import sqrt,pi,cos

F0 = 1.
x = 1.
n = 4.
m = 3.
v0 = 2.

v = sqrt(v0**2 + 2./m*(cos(x/n) - 1.) )

print "The velocity of the atom at position x = %g is v = %g"%(x,v)
