from numpy import sin, exp, linspace
import matplotlib.pyplot as plt
from ODESolver import ODESolver, ForwardEuler, RungeKutta4

Q0 = 0  # Initial electric charge, in Colomb
R = 1e8  # Resistance in Ohm
C = 2e-8  # Capasitance in Farad
timepoints = 101
seconds = 10
time_array = linspace(0, seconds, timepoints)
V0 = 8  # Voltage of battery when on

def Q_der(Q,t):  # Definition of Q'(t)
    return (V0 - Q/C)/R

# __Exercise a__
def Q_exact(t):  # Q(t) exact (only for charge-up).
    return (Q0 - C*V0)*exp(-t/(R*C)) + C*V0

circuit_FE = ForwardEuler(Q_der)
circuit_FE.set_initial_condition(Q0)
Q_FE, t = circuit_FE.solve(time_array)

circuit_RK4 = RungeKutta4(Q_der)
circuit_RK4.set_initial_condition(Q0)
Q_RK4, t = circuit_RK4.solve(time_array)

plt.plot(t, Q_FE, label='$Q(t)$, Forward Euler')
plt.plot(t, Q_RK4, label='$Q(t)$, Runge Kutta 4')
many_time_steps = linspace(0, seconds, 1001)  # For analytical solution.
plt.plot(many_time_steps, Q_exact(many_time_steps), label='$Q(t)$, exact')
plt.xlabel('Time [seconds]')
plt.ylabel('Electric charge [colomb]')
plt.title('Charging capasitor')
plt.legend()
plt.savefig('fig_E2.1.pdf')
plt.clf()

# __Exercise b__
def Q_der(Q,t):  # Redefining Q'(t) for exercise b
    if t < 10:
        V = 8
    elif t < 20:
        V = 4*sin(t) + 4
    else:
        V = 0
    return (V - Q/C)/R

time_array = linspace(0, 30, 101)
circuit_RK4_b = RungeKutta4(Q_der)
circuit_RK4_b.set_initial_condition(Q0)
Q_RK_b, t = circuit_RK4_b.solve(time_array)

plt.plot(t, Q_RK_b)
plt.xlabel('Time [seconds]')
plt.ylabel('Electric charge [colomb]')
plt.title('Charging, oscilating, and discharging capasitor')
plt.savefig('fig_E2.2.pdf')
plt.clf()
