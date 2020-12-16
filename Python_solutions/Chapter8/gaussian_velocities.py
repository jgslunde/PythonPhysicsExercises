import numpy as np
import random
import matplotlib.pyplot as plt

# __Exercise a__
m = 1e-22
T = 300.0
k = 1.38e-23
particles = 20
shape = (particles, 3)

s = np.sqrt(k*T/m)
vel = np.random.normal(0, s, shape)
print random.choice(vel)

# __Exercise b__
E_k = 0
for i in range(particles):
    E_k += 0.5*m*( vel[i,0]**2 + vel[i,1]**2 + vel[i,2]**2 )
print E_k, 3/2.0*k*T*particles
