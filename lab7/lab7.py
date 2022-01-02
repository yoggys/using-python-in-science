import numba
import numpy as np
import argparse
from math import exp, log, e, sqrt

kT = 2 / log(1 + sqrt(2), e)

def initParser():
    parser = argparse.ArgumentParser()
    #force -h to show groups in stdout
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument('--netsize', help="Size of net", type=int, required=True)
    required.add_argument('--jval', help="Value of J",type=float, required=True)
    required.add_argument('--bval', help="Value of Beta",type=float, required=True)
    required.add_argument('--heq', help="Equation for H (use TOT, NB, b, j values)", type=str, required=True)
    required.add_argument('--steps', help="Steps of simulation", type=int, required=True)
    optional.add_argument('--density', help="Initial spin density", type=float, default=0.5)
    optional.add_argument('--filename', help="Name of out images", type=str, default='step')
    return parser

@numba.jit(nopython=True)
def _update(net, i, j, eq):
    n, m = net.shape

    if "TOT" in eq:
        eq = eq.replace('TOT', str(net.sum()))

    if "NB" in eq:
        eq = eq.replace('TOT', 
            str(net[i, j] * (
                     net[(i-1)%n, (j-1)%m]
                   + net[(i-1)%n,  j     ]
                   + net[(i-1)%n, (j+1)%m]
                   + net[ i     , (j-1)%m]
                   + net[ i     , (j+1)%m]
                   + net[(i+1)%n, (j-1)%m]
                   + net[(i+1)%n,  j     ]
                   + net[(i+1)%n, (j+1)%m]
        )))

    dE = exec(eq)/2

    if dE <= 0 or exp(-dE / kT) > np.random.random():
        net[i, j] *= -1

@numba.jit(nopython=True)
def update(net, eq):
    n, m = net.shape

    for i in range(n):
        for j in range(0, m, 2):  # Even columns first to avoid overlap
            _update(net, i, j, eq)

    for i in range(n):
        for j in range(1, m, 2):  # Odd columns second to avoid overlap
            _update(net, i, j, eq)

if __name__ == '__main__':
    parser = initParser()
    args = parser.parse_args()

    eq = args.heq
    if "b" in eq:
        eq = eq.replace("b", str(args.bval))
    if "j" in eq:
        eq = eq.replace("j", str(args.jval))

    net = np.random.randint(2, size=(1000, 1000)).astype('i1')
    net[net == 0] = -1
    for i in range(100):
        update(net, eq)