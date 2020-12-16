import ODESolver
import numpy as np
import matplotlib.pyplot as plt

# a)
def temp_kettle(t):
    return 100

def f(u,t):
    k = 0.2
    t_env = temp_kettle(t)
    return -k*(u-t_env)

# b)
def temp_broken_kettle(t):
    return 20*np.sin(np.pi/3*t)+80

def f_broken(u,t):
    k = 0.2
    t_env = temp_broken_kettle(t)
    return -k*(u-t_env)


U0 = 15
T = 15      # Minutes
N = 10000

t_points = np.linspace(0,T+1,N)

solver = ODESolver.RungeKutta4(f)
solver.set_initial_condition(U0)
u,t = solver.solve(t_points)

temp_water = u

solver = ODESolver.RungeKutta4(f_broken)
solver.set_initial_condition(U0)
u,t = solver.solve(t_points)

temp_water_broken = u

plt.plot(t,temp_water,t,temp_water_broken)
plt.legend(['Slow','Broken'],loc='upper left')
plt.xlabel('Time [Minutes]')
plt.ylabel('Temperature')
plt.show()
