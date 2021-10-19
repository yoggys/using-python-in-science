import argparse
from simulate import Simulation

def initParser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--netsize', help="Size of net", type=int, required=True)
    parser.add_argument('--jval', help="Value of J",type=float, required=True)
    parser.add_argument('--bval', help="Value of Beta",type=float, required=True)
    parser.add_argument('--heq', help="Equation for H", type=str, required=True)
    parser.add_argument('--steps', help="Steps of simulation", type=int, required=True)
    parser.add_argument('--density', help="Initial spin density", type=float, default=0.5)
    parser.add_argument('--filename', help="Name of out images", type=str, default='step')

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
    