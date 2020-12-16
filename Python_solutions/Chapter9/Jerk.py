from constant_acceleration_class import ConstantAcceleration

class LinearAcceleration1(ConstantAcceleration):  # 'Is-a' relationship
    def __init__(self, x0, v0, a0, j):
        ConstantAcceleration.__init__(self, x0, v0, a0) # Let's superclass store values.
        self.j = j

    def __call__(self, t):  # Class call returns position.
        j = self.j
        return ConstantAcceleration.__call__(self, t) + 1.0/6*j**3

    def velocity(self, t):  # Method for returning velocity.
        j = self.j
        return ConstantAcceleration.velocity(self, t) + 0.5*j**2

class LinearAcceleration2:  # 'Has-a' relationship
    def __init__(self, x0, v0, a0, j):
        self.const_acc = ConstantAcceleration(x0, v0, a0)  # Creates instance of class
        self.j = j                                         # to store values.

    def __call__(self, t):
        j = self.j
        return self.const_acc(t) + 1.0/6*j**3

    def velocity(self, t):
        j = self.j
        return self.const_acc.velocity(t) + 0.5*j**2
