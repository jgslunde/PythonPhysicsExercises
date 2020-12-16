import matplotlib.pyplot as plt
from numpy import exp, cos, sqrt, linspace, zeros

def y(t, A, gamma, k, m):
    return A*exp(-gamma*t)*cos(sqrt(k/m)*t)

A = 0.3  # m
gamma = 0.15  # s^-1
k = 4.0  # km/s^2
m = 9.0  # kg

# __Exercise a__
length = 101  # length of arrays
time_interval = 25.0  # time interval we are studying
step_size = time_interval/(length - 1)  # time between two array elements

t_array = zeros(101)
y_array = zeros(101)
y_array[0] = A  # Initial position at t = 0

for i in range(length-1):
    t_array[i+1] = t_array[i] + step_size
    y_array[i+1] = y(t_array[i+1], A, gamma, k, m)


# __Exercise b__
t_array2 = linspace(0, time_interval, length)
y_array2 = y(t_array2, A, gamma, k, m)

plt.plot(t_array, y_array)
plt.plot(t_array2, y_array2)
plt.legend(["Exercise a y(t)", "Exercise b y(t)"])
plt.xlabel("Time [seconds]")
plt.ylabel("Amplitude [meters]")
plt.savefig("fig_oscilating_spring.pdf")
