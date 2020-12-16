from math import sqrt
G = 6.674*1E-11               #m^3*kg^(-1)*s^(-2)
M = 3.
N = 10

F = 0
for i in xrange(N):
    m_i = i/6. + 2
    r_i = sqrt((i/4.)**2 + 10)
    F += G*(m_i*M)/(r_i)**2

print "The total attractive force on the object with mass M = %g is %g N"%(M,F)
