"""
Pair Distribution Function
"""
import sys

from liquidlib.input_parser import InputParser, RdomainParser
from liquidlib.physical_quantity import PhysicalQuantity
from liquidlib.trajectory_factory import TrajectoryFactory


class PairDistributionFunction(PhysicalQuantity):
    """ Pair Distribution Function"""

    def __init__(self):
        pass

    def _prepare(self, input_file="g_r.in"):
        super()._prepare(input_file)
        self._parse_input()
        self._read_trajectory()

    def _parse_input(self):
        self.input_parser = RdomainParser()
        self.input_parameters = self.input_parser.parse(self.input_file)

    def _read_trajectory(self):
        self.trajectoryFactory = TrajectoryFactory(self.input_parameters["trajectory_file_name"])
        self.trajectory = self.trajectoryFactory.prepareTrajectory(self.input_parameters)

    def _compute(self):
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

    pair_distribution_function = PairDistributionFunction()
    print("%r" % pair_distribution_function)

    pair_distribution_function.execute(input_file)


if __name__ == '__main__':
    main()