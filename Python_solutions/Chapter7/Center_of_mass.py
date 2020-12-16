import numpy as np
class Particle:

    def __init__(self,position,mass):
        self.position = position
        self.mass = mass

if __name__ == '__main__':
    particles  = []
    for j in range(5):
        particles.append(Particle(np.array([j,2*j]),j*1e-30))

    total_mass = 0
    com = 0
    for particle in particles:
        total_mass += particle.mass
        com += particle.mass*particle.position
    com /= total_mass

    print "Center of mass in this system is:"
    print com
