#!/usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Lorentz(object):

    def __init__(self, init_state,
                 sigma = 10.0, rho=28.0, beta=2.67):

        assert init_state.shape == (3,)
        

        self.init_state = init_state
        self.state = None

        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def _diff(self, state_vector, t):

        x,y,z = state_vector

        xd = self.sigma * (y - x)
        yd = x * (self.rho - z) - y
        zd = x * y - self.beta * z

        return np.array([xd, yd, zd])
        
    def solve(self, start=0.0, end=30.0, step=0.01):

        print 'Solving ...',
        t = np.arange(start, end, step)
        self.state = odeint(self._diff, self.init_state, t)
        print 'done.'

    


if __name__ == '__main__':

    init_state = np.array([2.0, 3.0, 4.0])
    lorentz = Lorentz(init_state)
    lorentz.solve()
    
    # plotting the Lorentz attractor
    s = lorentz.state
    x,y,z = s[:,0], s[:,1], s[:,2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # ax = fig.gca(projection='3d')
    ax.plot(x,y,z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.savefig('/tmp/lorenz.png')
    # plt.show()
    
