"""
Quantity
~~~~~~~~~~~~~~~~

This is the base class for the physical quantities computed in liquidlib.

"""
from liquidlib.input_checker import InputChecker
from liquidlib.input_parser import InputParser
from liquidlib.trajectory_factory import TrajectoryFactory


class Quantity(object):
    """Abstract base class for quantities computed in liquidlib."""

    def __init__(self, input_file="quantity.in"):
        """Constructor of class Quantity

        :param input_file: input file defining computation parameters
        """
        self.input_file = input_file
        self.input_checker = InputChecker()
        self.trajectory_factory = TrajectoryFactory()

    def execute(self):
        """Executes all the procedures for calculation """
        self._parse_input()
        self._check_input()
        self._read_trajectory()
        self._compute()
        self._write()

    def _parse_input(self):
        """Parses input parameters from input file """
        self.input_parameters = InputParser.parse(self.input_file)

    def _check_input(self):
        """Check the validity of input parameters """
        self.input_checker.check(self.input_parameters)

    def _read_trajectory(self):
        """Read trajectory

        Instantiate a trajectory class using simple factory pattern,
        then read trajectory content
        """
        # self.input_parameters = dict()
        # self.input_parameters["trajectory_file_name"] = "test.trr"
        trajectory_file_name = self.input_parameters["trajectory_file_name"]
        self.trajectory = self.trajectory_factory.create_trajectory(trajectory_file_name)
        self.trajectory.read(self.input_parameters)

    def _compute(self):
        """Main logic to compute the quantity

        This method needs to be implemented in the derived class.
        """
        pass

    def _write(self):
        """Write the result to a file

        This method needs to be implemented in the derived class.
        """
        pass

    def __repr__(self):
        return "<class Quantity>: abstract base class for specific quantity."