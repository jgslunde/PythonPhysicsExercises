h = 6.626e-34  # Plancks constant, in Js
L = 1e-11  # size of box, in meters
m = 9.11e-31  # mass of particle, in kg

energies = []
total_energy = 0

for i in range(1, 30):  # From E1->E2 to E29->E30
    energy_step = (((i+1)**2-i**2)*h**2)/(8*m*L**2)
    energies.append(energy_step)
    total_energy += energy_step
