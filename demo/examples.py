__author__ = 'stephenhky'

import numpy as np

# 2D points
twoDpointseg1 = np.array([[0,0], [0,1], [1,0], [1,1.5], [2.2, 3.3], [0, 4], [5,1], [10, 10]])

# circular ring
ring = np.array([[np.cos(t), np.sin(t)] for t in np.linspace(0, 2*np.pi, 1001)])[1:]

# spherical ball
sphere = np.array([[np.sin(theta)*np.cos(phi), np.sin(theta)*np.sin(phi), np.cos(theta)] for theta in np.linspace(0.02, np.pi, 51) for phi in np.linspace(0.02, 2*np.pi, 51)])