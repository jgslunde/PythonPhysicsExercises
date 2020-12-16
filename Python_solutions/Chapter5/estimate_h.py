import matplotlib.pyplot as plt
import numpy as np

# a)
f = np.array([ 1.18,0.96,0.82,0.74])*1e15
E_max = np.array([ 3.12,1.57,0.8,0.22])*1e-19

plt.figure()
plt.plot(f,E_max,'ro')
plt.legend(['Data'],loc = 'upper left')
plt.xlabel('Frequency [Hz]')
plt.ylabel('E_max [J]')


# b)
h,w = np.polyfit(f,E_max,1)
print "Estimate of h: %g"%h

# c)
plt.figure()
plt.plot(f,E_max,'ro',f,h*f + w,'b')
plt.legend(['Data','Estimated line'],loc = 'upper left')

plt.show()
