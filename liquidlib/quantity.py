"""
PhysicalQuantity
~~~~~~~~~~~~~~~~

This is the base class for the physical quantities computed in liquidlib.

"""
from liquidlib.input_checker import InputChecker
from liquidlib.input_parser import InputParser
from liquidlib.trajectory_factory import TrajectoryFactory


class Quantity(object):
    """ Base class for physical quantities computed in liquidlib """

    def __init__(self, input_file="quantity.in"):
        self.input_file = input_file
        self.input_checker = InputChecker()
        self.trajectory_factory = TrajectoryFactory()

    def execute(self):
        """ This method executes all the procedures for calculation """
        self._parse_input()
        self._check_input()
        self._read_trajectory()
        self._compute()
        self._write()

    def _parse_input(self):
        """ This method parses input parameters from input file. """
        input_parser = InputParser()
        self.input_parameters = input_parser.parse(self.input_file)

    def _check_input(self):
        """ This method check the validity of input parameters. """
        self.input_checker.check(self.input_parameters)

    def _read_trajectory(self):
        # self.input_parameters = dict()
        # self.input_parameters["trajectory_file_name"] = "test.trr"
        trajectory_file_name = self.input_parameters["trajectory_file_name"]
        self.trajectory = self.trajectory_factory.create_trajectory(trajectory_file_name)
        self.trajectory.read(self.input_parameters)

    def _compute(self):
        """ This method contains the main logic to compute the quantity. """
        pass

    def _write(self):
        """ This methods write the result to a file. """
        pass

    def __repr__(self):
        return "<class PhysicalQuantity>: the base class for specific quantities."