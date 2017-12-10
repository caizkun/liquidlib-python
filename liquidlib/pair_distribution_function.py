"""
Pair Distribution Function
"""
import sys

from liquidlib.api.input_validator import RDomainQuantityValidator
from liquidlib.api.quantity import Quantity


class PairDistributionValidator(RDomainQuantityValidator):
    pass


class PairDistributionFunction(Quantity):
    """
    Pair Distribution Function
    """

    def __init__(self, input_file="g_r.in"):
        """
        Constructor of PairDistributionFunction class

        :param input_file: input file defining the computation parameters
        """
        super().__init__(input_file)
        self.input_checker = PairDistributionValidator()

    def _compute(self):
        """
        Main logic to compute the quantity
        """
        selected_atom_indexes = self._atom_selector.select(self.input_parameters, self.trajectory)

        # ---------------------------------
        # implement the headache logic here
        # ---------------------------------
        pass

    def _write(self):
        """
        Write the result to a file
        """
        # TODO: may use a Util class
        pass

    def __repr__(self):
        return "<class PairDistributionFunction>"


# --- Demo of extension ---
class DemoPairDistributionFunction(PairDistributionFunction):
    """
    A demo class that extends class PairDistributionFunction
    """
    def _compute(self):
        pass


def main():
    """
    Compute the pair distribution function
    """
    input_file = "g_r.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])

    pair_distribution_function = PairDistributionFunction(input_file)

    print(pair_distribution_function.input_file)
    print("%r" % pair_distribution_function)

    # Below demonstrate a few more customizations available if needed.
    # If these customizations still do not fit your needs, you may consider
    # inheriting the specific quantity your are interested in, and override
    # some of the methods.

    # if using a new strategy to select atoms
    # pair_distribution_function.atom_selector = SelectByAtomId()

    # if validating new parameters provided in the input file
    # pair_distribution_function.input_validator = DemoPairDistributionInputValidator()

    # if reading a new uncommon trajectory type
    # pair_distribution_function.trajectory_factory = DemoTrajectoryFactory()

    pair_distribution_function.execute()


if __name__ == '__main__':
    main()