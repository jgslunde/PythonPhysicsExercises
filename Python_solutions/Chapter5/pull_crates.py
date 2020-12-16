import numpy as np
# a)
N = 10
F = [0]*N
for i in xrange(N):
    F[i] = 30 + 5*i

# b)
F = np.array(F)
F = F/2.
print "Total forces: %g N"%np.sum(F)
