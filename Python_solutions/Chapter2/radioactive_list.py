from math import exp, log

N0 = 4.5
N = N0
t = 0; dt = 60
tau = 1760.0
t_list = [t]; N_list = [N]  # Including initial time and mass in list.

# __Exercise a__
while N > 0.5*N0:
    t += dt
    N = N0*exp(-t/tau)
    N_list.append(N)
    t_list.append(t)
print "%.2f%% is left of the carbon-11 after %d seconds." % (N/N0*100, t)


# __Exercise b__
print "Estimated half-life from simulation = %.2f s" % t_list[-1]
print "Actual half-life from analytical solution = %.2f s" % (tau*log(2))


# __Exercise c__
Nt = []
for i in range(len(t_list)):
    Nt.append([t_list[i], N_list[i]])

print "\n%12s%12s" % ("t [Seconds]","N(t) [Kg]")
for i in range(len(t_list)):
    print "%11d%12.4g" % (Nt[i][0], Nt[i][1])

# __Exercise c, alternative solution__
Nt = []
for t, N in zip(t_list, N_list):
    Nt.append([t,N])

print "\n%12s%12s" % ("t [Seconds]","N(t) [Kg]")
for Nt_pair in Nt:
    print "%11d%12.4g" % (Nt_pair[0], Nt_pair[1])
