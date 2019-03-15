import numpy as np

np.random.seed(123)

class Robot():
    """
    2D point mass two input along x and y axis
    """

    def __init__(self, mass=1.):

        self._mass = mass

    def dynamics(self, x, u):
        """
        Params: x = state vector, type np.array, dim = 4
                u = control command, type np.array dim = 2
        """

        #x1 = x, x2 = y, x3 = x_dt, x4 = y_dt
        x1, x2, x3, x4 = x
        x1_dt, x2_dt =  x3, x4
        x3_dt = u[0]/self._mass
        x4_dt = u[1]/self._mass

        return [x1_dt, x2_dt, x3_dt, x4_dt]


class RK4Int():
    """
    Runge Kutta 4rth Order integrator
    expects a ode_fn that takes in two inputs
    """

    def __init__(self, ode_fn, dt=0.001, step_size=0.01):

        self._ode_fn = ode_fn

        self._dt = dt

        self._step_size = step_size

    def average(self, x):
        """
        Agnotstic to dim of x
        """

        x_i, k1, k2, k3, k4 = x

        return x_i + (k1 + 2.0*(k3 + k4) +  k2) / 6.0

    def rk4_step(self, x, u, dt):
        """
        Agnotstic to dim of x and u
        """

        dx = self._ode_fn(x, u)

        k2 = [ dx_i*dt for dx_i in dx ]

        xv = [x_i + delx0_i/2.0 for x_i, delx0_i in zip(x, k2)]
        k3 = [ dx_i*dt for dx_i in self._ode_fn(xv, u)]

        xv = [x_i + delx1_i/2.0 for x_i,delx1_i in zip(x, k3)]
        k4 = [ dx_i*dt for dx_i in self._ode_fn(xv, u) ]

        xv = [x_i + delx1_2 for x_i,delx1_2 in zip(x, k4)]
        k1 = [self._dt*i for i in self._ode_fn(xv, u)]

        self._t += dt

        return np.asarray(map(self.average, zip(x, k1, k2, k3, k4)))


    def integrate(self, x, u, t=0):
        """
        Agnotstic to dim of x and u
        """

        self._t = 0

        while self._t <= self._step_size:

            x = self.rk4_step(x, u, self._dt)

        return x



def main():
    """
    Test code
    """

    robot = Robot()

    rk4 =  RK4Int(robot.dynamics)

    x = np.random.randn(4)

    for i in range(100):

        x = rk4.integrate(x, np.random.randn(2))

        print("State %d is"%i), np.round(x, 2)


if __name__ == '__main__':

    main()
