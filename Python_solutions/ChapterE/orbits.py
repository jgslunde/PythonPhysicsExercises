from numpy import sqrt, pi, linspace
import matplotlib.pyplot as plt
from ODESolver import ODESolver, ForwardEuler, RungeKutta4

def f(u,t):
    M = 1  # SolarMasses
    G = 4*pi**2  # AU^3/(yr^2*SM)
    x, y, vx, vy = u
    dx = vx
    dy = vy
    radius = sqrt(x**2 + y**2)
    dvx = -G*M*x/radius**2
    dvy = -G*M*y/radius**2
    return [dx, dy, dvx, dvy]

planet = RungeKutta4(f)
x = 1; y = 0  # AU
vx = 0; vy = 2*pi  # AU/yr
U0 = [x, y, vx, vy]
planet.set_initial_condition(U0)

time_points = linspace(0,10,1001)
u, t = planet.solve(time_points)

x, y, vx, vy = u[:,0], u[:,1], u[:,2], u[:,3]

plt.plot(x, y)
plt.axis('equal')
plt.show()
