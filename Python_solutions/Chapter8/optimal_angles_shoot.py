import numpy as np
import random

def height(t,v0,alpha):
    g = 9.81
    return -.5*g*t**2 + v0*t*np.sin(alpha)

def find_hit_alphas(v0,b,h0,h1,alphas):
    hit_alpha = []
    for a in alphas:
        T = b/(v0*np.cos(a))
        y = height(T,v0,a)
        if (h0 <= y <= h1):
            hit_alpha.append(a)
    return hit_alpha

h0 = 3
h1 = 3.25
b = 3.5
g = 9.81

v0 = 25.
N = 1000
alphas = np.random.uniform(0,np.pi,N)

found_alphas_uni = find_hit_alphas(v0,b,h0,h1,alphas)
while(found_alphas_uni == []):
    alphas = np.random.uniform(0,np.pi,N)
    found_alphas_uni = find_hit_alphas(v0,b,h0,h1,alphas)


mean_alpha = np.mean(found_alphas_uni)
alphas = np.random.normal(mean_alpha,.05,N)
found_alphas_norm = find_hit_alphas(v0,b,h0,h1,alphas)

print "Number of found alphas using uniform: %d"%len(found_alphas_uni)
print "Number of found alphas using normal with mean = %g: %d"\
%(mean_alpha,len(found_alphas_norm))
