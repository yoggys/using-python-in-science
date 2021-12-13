
import argparse
import numpy as np
from time import sleep

def simplify(m):
    m = m.round().astype(int).A1
    lcm = np.gcd.reduce(m)
    m = np.append(m, m.sum())
    return (m / lcm).astype(int)

def check_state(m):
    active, terminal = [], []
    for row in range(len(m)):
        if sum(m[row]) == 0:
            terminal.append(row)
        else:
            active.append(row)
    return active, terminal

def solution(m):
    # check for absorbing (Markov chain)
    active, terminal = check_state(m)

    if 0 in terminal:
        return [1] + [0 for _ in terminal[1:]] + [1]

    #rearrange matrix
    m = np.matrix(m, dtype=float)[active, :]
    rearranged = m / m.sum(1)

    # get RQ
    R = rearranged[:, terminal]
    Q = rearranged[:, active]

    #calculate F = (I-Q)^-1
    F = np.linalg.inv((np.identity(len(Q)) - Q))
    
    #calculate FR and parse to fractions format
    FR = F[0] * R * np.prod(m.sum(1)) / np.linalg.det(F)
    return simplify(FR)

# decorator
def task_timer(*args, **kwargs):
    def inner(func):
        def execute(func):
            if func is None: return True
            func()
            sleep(kwargs['delay'])

        if kwargs['loop'] is None:
          while True:
            if execute(func): break
        else:
            for _ in range(kwargs['loop']):
              if execute(func): break

    return inner

def initParser():
    parser = argparse.ArgumentParser()
    parser._action_groups.pop()

    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('--loop', help="Loop execute amount, default inf", type=int, default=None)
    optional.add_argument('--delay', help="Loop delay time in seconds", type=float, default=1.)

    return parser

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    @task_timer(loop=args.loop, delay=args.delay)
    def calculate():
        # solution(np.random.randint(5, size=(6, 6)))
        print(solution([
            [0,1,0,0,0,1],
            [4,0,0,3,2,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
        ]))

    try:
        calculate()
    except Exception as E:
        pass
    