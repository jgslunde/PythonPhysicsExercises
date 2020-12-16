from math import pi

# __Exercise a__
class Planet:
    def __init__(self, name, radius, mass):
        self.name = name
        self.radius = radius
        self.mass = mass

    def density(self):
        return mass / 4/3.0*pi*r**3

    def print_info(self):
        print "The planet %s has a radius %.2f, a mass %.2f, and a density %.2f" % \
        (self.name, self.radius, self.mass, self.density())

# __Exercise b__
planet1 = Planet("Earth", 10, 10)
planet1.population = 7497486172
print planet1.name, "has a population of", planet1.population
