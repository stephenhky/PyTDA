__author__ = 'stephenhky'

import matplotlib.pyplot as plt
import pylab
import numpy as np
import simcomplex
import demo.examples as eg

def calculate_alpha_betti0(points, epsilon, complexclass):
    sc = complexclass(points, epsilon)
    return sc.betti_number(0)

epsilons = np.linspace(0, 2, 101)

alpha_betti0s = map(lambda epsilon: calculate_alpha_betti0(eg.twoDpointseg1, epsilon, simcomplex.AlphaComplex),
                    epsilons)

vr_betti0s = map(lambda epsilon: calculate_alpha_betti0(eg.twoDpointseg1, epsilon, simcomplex.VietorisRipsComplex),
                 epsilons)

plt.plot(epsilons, alpha_betti0s)
plt.plot(epsilons, vr_betti0s)

pylab.show()