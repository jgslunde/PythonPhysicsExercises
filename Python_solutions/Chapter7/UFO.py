from math import sqrt

# __Exercise a__
class ObjectMovement:
    def __init__(self, x0, y0, vx0, vy0, a=-9.81):
        self.x0, self.y0, self.vx0, self.vy0, self.a = x0, y0, vx0, vy0, a

    def position(self, t):
        x = self.x0 + self.vx0*t
        y = self.y0 + self.vy0*t + 0.5*self.a*t**2
        return x, y

    def velocity(self, t):
        vx = self.vx0
        vy = self.vy0 + self.a*t
        return vx, vy

def test_pos_vel():
    x0 = 10; y0 = 20; vx0 = 5; vy0 = 30; a = -9.81; t = 3; tol = 1e-6
    ball = ObjectMovement(x0,y0,vx0,vy0,a)

    x1_calc = 25; y1_calc = 65.855
    vx1_calc = 5; vy1_calc = 0.57

    x1, y1 = ball.Position(t)
    vx1, vy1 = ball.Velocity(t)

    assert abs(x1 - x1_calc) < tol and abs(y1 - y1_calc) < tol,\
    "Position doesn't match"
    assert abs(vx1 - vx1_calc) < tol and abs(vy1 - vy1_calc) < tol,\
    "Velocity doesn't match"

# __Exercise b__
def test_energy_conservation():
    x0 = 10; y0 = 20; vx0 = 5; vy0 = 30; a = -9.81; t = 3; tol = 1e-6
    ball = ObjectMovement(x0,y0,vx0,vy0,a)
    v0 = sqrt(vx0**2 + vy0**2)
    Ek0 = 0.5*v0**2
    Ep0 = - a*y0

    x1, y1 = ball.Position(t)
    vx1, vy1 = ball.Velocity(t)
    v1 = sqrt(vx1**2 + vy1**2)
    Ek1 = 0.5*v1**2
    Ep1 = - a*y1

    assert abs((Ek0+Ep0)-(Ek1+Ep1)) < tol, "Energy not conserved"
