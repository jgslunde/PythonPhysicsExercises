import numpy as np
import ODESolver
import matplotlib.pyplot as plt

class Problem:
    def __init__(self,U0,r,w):
        self.U0 = U0

        self.g = 9.81
        self.r = r               # given in m
        self.rho = 1.293         # kg/m^3
        self.C = 0.47
        self.m = 0.057           # given in kg
        self.w = w               # given in m/s

    def __call__(self,u,t):
        x,vx,y,vy = u
        return [vx,-(self.rho*self.r**2*np.pi*self.C*(vx-self.w)**2)/(2*self.m),vy,-self.g]

if __name__ == '__main__':

    x0 = 0; y0 = 0

    alpha = np.pi/4
    v0 = 10.

    U0 = [x0,v0*np.cos(alpha),y0,v0*np.sin(alpha)]
    T = 0.5
    N = 1000

    t_points = np.linspace(0,T+1,N)

    labels = []
    plt.hold('on')
    for w in [-10,-5,0,5,10]:
        problem = Problem(U0,0.03275,w)

        solver = ODESolver.RungeKutta4(problem)
        solver.set_initial_condition(problem.U0)

        u,t = solver.solve(t_points)

        x = u[:,0]
        y = u[:,2]
        labels.append('w = %g'%w)
        plt.plot(x,y)
    plt.xlabel('Position along ground [m]')
    plt.ylabel('Height [m]')
    plt.legend(labels)
    plt.savefig('fig_air_resistance.pdf')
    plt.show()
