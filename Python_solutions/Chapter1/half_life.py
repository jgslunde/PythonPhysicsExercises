from math import exp, log

N0 = 4.5  #kg
t = 10.0*60  #s
# Exercise a)
tau = 1760
N = N0*exp(-t/tau)
print "Remaining weight of carbon-11 is %.4g kg" % N

# Exercise b)
t_half = 1220  #s
tau = t_half/log(2)
N = N0*exp(-t/tau)
print "Remaining weight of carbon-11 is %.4g kg" % N

"""
Remaining weight of carbon-11 is 3.2 kg
Remaining weight of carbon-11 is 3.2 kg
"""
