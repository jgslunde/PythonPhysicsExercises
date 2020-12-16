def x(t, v0, q, E, m):
    return v0*t + 0.5*q*E/m*t**2

def v(t, v0, q, E, m):
    return v0 + q*E/m*t

m_electron = 9.1e-31
q_electron = -1.6e-19
E = 1e-10

# __Exercise a__
v0 = float(raw_input("Initial velocity of electron: "))
t = float(raw_input("Time at which we wish to study the electron: "))
x_value = x(t, v0, q_electron, E, m_electron)
v_value = v(t, v0, q_electron, E, m_electron)
print "Electron has a position of %.2f m and a velocity of %.2f m/s \
at time %.2f seconds." % (x_value, v_value, t)


# __Exercise b__
import sys
try:
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
    q = float(sys.argv[3])
    m = float(sys.argv[4])
except IndexError:
    print "Too few command line arguments."
    v0 = float(raw_input("Initial velocity of particle: "))
    t = float(raw_input("Time at which we wish to study the particle: "))
    q = float(raw_input("Charge of particle: "))
    m = float(raw_input("Mass of particle: "))
except ValueError:
    print "Input cannot be converted to float."
    v0 = float(raw_input("Initial velocity of particle: "))
    t = float(raw_input("Time at which we wish to study the particle: "))
    q = float(raw_input("Charge of particle: "))
    m = float(raw_input("Mass of particle: "))

x_value = x(t, v0, q, E, m)
v_value = v(t, v0, q, E, m)
print "Particle has a position of %.2f m and a velocity of %.2f m/s \
at time %.2f seconds." % (x_value, v_value, t)
