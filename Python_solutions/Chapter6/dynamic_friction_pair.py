# Her er det viktig at de faar til split riktig

# a)
with open('friction_coefficients_data.dat','r') as infile:
    materials = infile.readline().split()
    values = infile.readline().split()

# b)
m = 2.5
g = 9.81
print "Material of object | Material of surface | Dynamic friction"
for i,pair in enumerate(materials):
    mat = pair.split('-')
    N = m*g*float(values[i])
    print "%10s  %20s  %20g "%(mat[0],mat[1],N)
