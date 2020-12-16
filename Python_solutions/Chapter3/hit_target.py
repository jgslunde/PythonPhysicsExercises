from math import cos,pi,sin

def height(t,v0,th):
    g = 9.81
    return -.5*g*t**2 + v0*t*sin(th)

def find_points(h0,h1,y):
    points = 0
    mid_point = (h0 + h1)/2.
    if (h0 <= y <= mid_point):
        points = 1
    elif (mid_point < y <= h1 ):
        points = 2
    return points

h0 = 3
h1 = 3.5
b = 3.5
g = 9.81
th = pi/4

for v0 in [15.,16.,19.,22.]:
    T = b/(v0*cos(th))
    y = height(T,v0,th)
    print "Number of points using v0 = %g: %g"%(v0,find_points(h0,h1,y))
