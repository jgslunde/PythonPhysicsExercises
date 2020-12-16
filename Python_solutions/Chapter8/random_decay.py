import numpy as np
import random
import matplotlib.pyplot as plt

# __Exercise a+b__
number_of_atoms = 40
seconds = 30
p = 0.0926

atoms_array = np.ones(number_of_atoms)
atoms_over_time = np.zeros(seconds+1)
atoms_over_time[0] = number_of_atoms

for t in range(seconds):
    for i in range(number_of_atoms):
        if atoms_array[i] == 1:
            if random.random() < p:
                atoms_array[i] = 0
    atoms_over_time[t+1] = np.sum(atoms_array)

# __Exercise c__
tau = 10.3
time = np.linspace(0, seconds, seconds+1)
plt.plot(time, atoms_over_time)
plt.plot(time, number_of_atoms*np.exp(-time/tau))
plt.axis([0, seconds, 0, number_of_atoms])
plt.savefig("fig_random_decay.pdf")
