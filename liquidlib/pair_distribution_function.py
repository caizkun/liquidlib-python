"""
Pair Distribution Function
"""
import sys

from liquidlib.input_checker import PairDistributionInputChecker
from liquidlib.quantity import Quantity


class PairDistributionFunction(Quantity):
    """ Pair Distribution Function """

    def __init__(self, input_file="g_r.in"):
        super().__init__(input_file)
        self.input_checker = PairDistributionInputChecker()

    def _compute(self):
        """ main logic to compute the quantity """
        pass

    def _write(self):
        pass

    def __repr__(self):
        return "<class PairDistributionFunction>"


def main():
    """ main function to compute pair distribution function """

    input_file = "g_r.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])
    print(input_file)

    pair_distribution_function = PairDistributionFunction(input_file)
    print("%r" % pair_distribution_function)

    pair_distribution_function.execute()


if __name__ == '__main__':
    main()