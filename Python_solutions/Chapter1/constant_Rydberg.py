me = 9.109e-31          #m
e = 1.602e-19           #C
varepsilon = 8.854e-12  #CV^{-1}m^{-1}
h = 6.626e-34           #Js
c = 3e8                 #m/s

rydberg = me*e**4/(8*varepsilon**2*h**3*c)
print "The Rydberg constant is approximately: %g m^{-1}"%rydberg
