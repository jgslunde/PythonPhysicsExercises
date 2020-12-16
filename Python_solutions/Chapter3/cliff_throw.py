from math import sqrt

# __Exercise a__
def velocity1(t, v0, a=9.81):
    return v0 + a*t

def velocity2(x, v0, a=9.81):
    return sqrt(v0**2 + 2*a*x)

# __Exercise b__
def test_velocity():
    tol = 1e-6
    v0 = 5.5
    t = 3.5
    a = 9.81
    x = v0*t + 0.5*a*t**2

    v1 = velocity1(t, v0)
    v2 = velocity2(x, v0)

    assert (v1 - v2) < tol, "The two functions return different velocities."

# __Exercise c__
def velocity1_improved(t, v0, a=9.81):
    if type(t) is list:
        v = []
        for t_element in t:
            v.append(v0 + a*t_element)
        return v
    else:
        return v0 + a*t
