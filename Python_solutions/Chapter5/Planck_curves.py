import numpy as np
import matplotlib.pyplot as plt

h = 6.62e-34
k = 1.38e-23
c = 3e8
wavelengths = np.linspace(1e-8, 3e-6, 1001)

def B(lamb, T):
    return 2*h*c**2/lamb**5*1/(np.exp(h*c/(lamb*k*T))-1)

# __Exercise a__
T_Sun = 5772.0
plt.plot(wavelengths, B(wavelengths, T_Sun))
plt.xlabel("$\lambda$ [m]")
plt.ylabel("B($\lambda$)")
plt.savefig("fig_Planck_curves_a.pdf")
plt.clf()

# __Exercise b__
T_Alpha = 5160.0
T_Proxima = 3042.0
plt.plot(wavelengths, B(wavelengths, T_Sun), color = "b", label = "Sun")
plt.plot(wavelengths, B(wavelengths, T_Alpha), color = "r", label = "Alpha Centauri")
plt.plot(wavelengths, B(wavelengths, T_Proxima), color = "g", label = "Proxima Centauri")
plt.xlabel("$\lambda$ [m]")
plt.ylabel("B($\lambda$)")
plt.legend()
plt.savefig("fig_Planck_curves_b.pdf")
plt.clf()

# __Exercise c__
b = 2.9e-3
lamb_max_Sun = b/T_Sun
lamb_max_Alpha = b/T_Alpha
lamb_max_Proxima = b/T_Proxima

plt.plot(wavelengths, B(wavelengths, T_Sun), color = "b", label = "Sun")
plt.plot(wavelengths, B(wavelengths, T_Alpha), color = "r", label = "Alpha Centauri")
plt.plot(wavelengths, B(wavelengths, T_Proxima), color = "g", label = "Proxima Centauri")
plt.xlabel("$\lambda$ [m]")
plt.ylabel("B($\lambda$)")
plt.axvline(x=lamb_max_Sun, ls="--", color = "b")
plt.axvline(x=lamb_max_Alpha, ls="--", color = "r")
plt.axvline(x=lamb_max_Proxima, ls="--", color = "g")
plt.legend()
plt.savefig("fig_Planck_curves_c.pdf")
plt.clf()
