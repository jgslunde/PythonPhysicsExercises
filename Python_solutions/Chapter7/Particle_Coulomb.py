import numpy as np

# a)
class Particle:

    def __init__(self,position,q):
        self.position = position
        self.q = q

    def interact(self,other_particle):
        pos = self.position
        pos_other = other_particle.position
        r = np.linalg.norm(pos-pos_other)

        q = self.q
        q_other = other_particle.q

        ke = 8.998*1e9       # N m^2/C^2

        return abs(ke*q*q_other/r**2)

# b)
def test_interaction():
    p1 = Particle(np.array([0,0]),-1.602*1e-19)
    p2 = Particle(np.array([0,30*1e-3]),1.602*1e-19)
    F = p1.interact(p2)
    expected = 2.565833688*1e-15
    assert abs(F-expected)<1e-14,'Expected: %g, got: %g'%(expected,F)

if __name__ == '__main__':
    test_interaction()
