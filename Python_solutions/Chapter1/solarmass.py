from math import pi

AU = 1.58*1E-5       # 10^(-5)   lysaar
ly = 9.5*1E15        # 10^(15)   m
G = 6.674*1E-11       # 10^(-11) m^3*kg^(-1)*s^(-2)

AU_km = AU*ly                               # 10^(10) km

yr = 365*24*60*60                       # 10^(7) s
M_sun = (4*pi**2*(AU_km)**3)/(G*(yr)**2)    # 10^(27)

print "The calculated solar mass is: %g kg"%M_sun
