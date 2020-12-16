# Definition expected in a)
class GeometricShape:
    def __init__(self,mass):
        self.mass = mass

# Definition expected in b)
class Cylinder(GeometricShape):
    def __init__(self,mass,r):
        GeometricShape.__init__(self,mass)
        self.r = r

    def inertia(self):
        M = self.mass
        R = self.r
        return .5*M*R**2

# Definition expected in c)
class CylindricalShell(Cylinder):

    def inertia(self):
        return 2*Cylinder.inertia(self)

if __name__ == '__main__':
    # usage expected in a)
    shape = GeometricShape(5)

    # usage expected in b)
    cylinder = Cylinder(5,0.75)
    print "Cylinder has moment of inertia I = %g"%cylinder.inertia()

    # usage expected in c)
    cylinder_s = CylindricalShell(5,0.75)
    print "Cylindrical shell has moment of inertia I = %g"%cylinder_s.inertia()
