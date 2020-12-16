v0 = 0
g = 9.81
dt = 0.01
h0 = 10
h1 = 5

time_taken = 0
current_height = h0
while(current_height > h1):
    time_taken += dt
    current_height = v0*time_taken - .5*g*time_taken**2+h0

print "It took the ball approximately %g seconds to pass %g meters"%(time_taken,h1)
