def quantum_energy(n1, n2, L, m):
    h = 6.626e-34
    E1 = (n1**2*h**2)/(8*m*L**2)
    E2 = (n2**2*h**2)/(8*m*L**2)
    return E2 - E1
