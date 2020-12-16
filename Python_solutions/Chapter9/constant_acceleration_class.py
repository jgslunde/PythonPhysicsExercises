class ConstantAcceleration:
    def __init__(self, x0, v0, a0):
        self.x0 = x0
        self.v0 = v0
        self.a0 = a0

    def __call__(self, t):
        x0 = self.x0; v0 = self.v0; a0 = self.a0
        return x0 + v0*t + 0.5*a0*t**2

    def velocity(self, t):
        x0 = self.x0; v0 = self.v0; a0 = self.a0
        return v0 + a0*t
