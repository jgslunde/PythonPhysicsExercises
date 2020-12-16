# a)
def x(t,f,v0):
    return v0*t - .5*f*9.81*t**2

# b)
def find_distance(v0,dt,frictions):
    g = 9.81
    t = 0
    v = v0
    
    l = len(frictions)
    lengths = [0]*l
    for i in range(l):

        f = frictions[i]

        while(v > 0):
            t += dt
            v = v0 - f*g*t

        lengths[i] = v0*t - .5*f*g*t**2
        v = v0
        t = 0
    return lengths

# c)
def test_find_distance(lengths,frictions,v0):
    for f,l in zip(frictions,lengths):
        T = v0/(f*9.81)
        expected_length = x(T,f,v0)
        assert abs(expected_length-l)<1E-7 , \
        'Expected: %g, got: %g'%(expected_length,l)


frictions = [0.62,0.3,0.45,0.2]
v0 = 5.

lengths = find_distance(v0,0.0001,frictions)
test_find_distance(lengths,frictions,v0)
