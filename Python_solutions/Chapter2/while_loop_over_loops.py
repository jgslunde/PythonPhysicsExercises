from math import sqrt

g = 9.81
r = [2.7,3.43,5.62,7.1]
num_loops = len(r)
v = [0]*num_loops

i = 0
while i < num_loops:
    v[i] = sqrt(r[i]*g)     #in m/s
    v[i] = v[i]*3600/1000   #convert to km/h
    print "Least speed to complete the loop: %.2f km/h"%v[i]
    i += 1
