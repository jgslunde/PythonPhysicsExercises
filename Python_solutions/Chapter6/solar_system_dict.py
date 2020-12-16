# __Exercise a__
with open("solar_system_data.dat", "r") as infile:
    infile.readline(); infile.readline()  # Skipping two first lines.
    distance = {}
    mass = {}
    radius = {}
    for line in infile:
        words = line.split()
        distance[words[0]] = float(words[1])
        mass[words[0]] = float(words[2])
        radius[words[0]] = float(words[3])

# __Exercise b__
from math import pi
density = {}
for planet in mass:  # Looping over a dictionary gives its keys.
    planet_volume = 4.0/3*pi*(radius[planet]*1000)**3
    density[planet] = mass[planet]/planet_volume

# __Exercise c__
with open("solar_system_data2.dat", "w") as outfile:
    outfile.write("%8s %16s %16s %16s %16s\n" % ("Object", "Distances[km]", "Mass[kg]", "Radius[km]", "Densities[kg/m^3]"))
    for planet in mass:
        outfile.write("%8s %16.2e %16.2e %16d %16d\n" % (planet, distance[planet], mass[planet], radius[planet], density[planet]))

# __Exercise d__
solar_system = {}
for planet in mass:
    solar_system[planet] = {}
    solar_system[planet]["mass"] = mass[planet]
    solar_system[planet]["distance"] = distance[planet]
    solar_system[planet]["radius"] = radius[planet]
    solar_system[planet]["density"] = density[planet]

number_of_earths = solar_system["Pluto"]["distance"]/solar_system["Earth"]["radius"]
print "Number of earths from Sun to Pluto = %.2f" % number_of_earths
