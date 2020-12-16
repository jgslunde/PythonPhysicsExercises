from math import exp

def N(N0, tau, t):
    return N0*exp(-t/float(tau))

def test_N():
    tol = 1e-4
    calculated_N = N(4.5, 1760, 600)
    actual_N = 3.2
    assert abs(actual_N - calculated_N) < tol

test_N()
