#a)
d = {}
with open('physics_constants.dat','r') as infile:
    for line in infile:
        data = line.split()
        name = data[-3]
        value = float(data[-2])
        d[name] = value

#b)
ke = d['ke']
me = d['me']
e = d['e']
hbar = d['hbar']

factor = (ke**2*me*e**4)/(2*hbar**2)
print "In J: %g\nIn eV: %g"%(factor,factor/e)
