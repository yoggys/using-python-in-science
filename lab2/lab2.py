import argparse
from simulate import Simulation

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

if __name__ == "__main__":
    parser = initParser()
    args = parser.parse_args()

    s = Simulation(
        size=args.netsize,
        j=args.jval,
        b=args.bval,
        h=args.heq,
        steps=args.steps,
        density=args.density,
        filename=args.filename
    )

    s.start()
    del s
    