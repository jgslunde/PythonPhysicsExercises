from math import sin,sqrt,pi # Eventually import from numpy
class Runner:
    #a)
    def __init__(self,mass,v0,alpha):
        self.mass = float(mass)
        self.v0 = float(v0)
        self.alpha = float(alpha)

    #b)
    def __str__(self):
        return "Sprinter with \n mass: %g kg \n initial velocity: %g m/s\n angle: %g degrees"\
        %(self.mass,self.v0,self.alpha)

    #c)
    def finish_runtime(self,dist):
        g = 9.81
        F_ = 400

        m = self.mass
        a = self.alpha
        v0 = self.v0

        # Remember to convert to radians
        p_ = g*sin(a*pi/180) + (1./m)*F_

        return -v0/p_ + sqrt(v0**2 + 2*dist*p_)/p_

if __name__ == '__main__':
    r1 = Runner(80,5,30)
    print r1

    dist = 100;
    print "Finish runtime for distance %g m: %g s"%(dist,r1.finish_runtime(dist))
