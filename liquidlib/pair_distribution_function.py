"""
Pair Distribution Function
"""
import sys

from liquidlib.atom_selector import AtomSelector
from liquidlib.input_checker import RDomainInputChecker
from liquidlib.quantity import Quantity


class PairDistributionInputChecker(RDomainInputChecker):
    pass


class PairDistributionFunction(Quantity):
    """Pair Distribution Function"""

    def __init__(self, input_file="g_r.in"):
        """Constructor of PairDistributionFunction class

        :param input_file: input file defining the computation parameters
        """
        super().__init__(input_file)
        self.input_checker = PairDistributionInputChecker()

    def _compute(self):
        """Main logic to compute the quantity"""
        # select atoms of interest
        atom_selector = AtomSelector()

        # do the heavy lifting here
        pass

    def _write(self):
        """Write the result to a file"""
        # TODO: may use a Util class
        pass

    def __repr__(self):
        return "<class PairDistributionFunction>"


def main():
    """Compute the pair distribution function"""
    input_file = "g_r.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])
    print(input_file)

    pair_distribution_function = PairDistributionFunction(input_file)
    print("%r" % pair_distribution_function)

    pair_distribution_function.execute()


if __name__ == '__main__':
    main()