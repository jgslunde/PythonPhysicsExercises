def x(t,f,v0):
    return v0*t - .5*f*9.81*t**2

def find_distance(v0,dt,frictions):
    g = 9.81
    v = v0
    l = len(frictions)
    lengths = [0]*l
    for i in range(l):
        f = frictions[i]
        T = v0/(f*9.81)
        lengths[i] = x(T,f,v0)
    return lengths


frictions = [0.62,0.3,0.45,0.2]
v0 = 5.

lengths = find_distance(v0,0.0001,frictions)
for l,f in zip(lengths,frictions):
    print "Length: %g with frictioncoefficient: %g "%(l,f)
