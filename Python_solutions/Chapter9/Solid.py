# a)
class Solid:
    def __init__(self,volume):
        self.volume = volume

    def mass_density(self,mass):
        return mass/self.volume

# b)
class Iron(Solid):
    def __init__(self,volume,mass):
        Solid.__init__(self,volume)
        self.mass = mass

    def density(self):
        return Solid.mass_density(self,self.mass)


# c)
def test_density():
    body = Iron(0.1,787)
    expected = 7870.
    cal = body.density()

    assert abs(cal - expected) < 1e-14, 'Got: %g, expected: %g'\
    %(cal,expected)

if __name__ == '__main__':
    test_density()
