"""
Quantity
~~~~~~~~~~~~~~~~

This is the base class for the physical quantities computed in liquidlib.

"""
from abc import ABC, abstractmethod

from liquidlib.atom_selector import AtomSelector
from liquidlib.input_checker import InputChecker
from liquidlib.input_parser import InputParser
from liquidlib.trajectory_factory import TrajectoryFactory


class Quantity(ABC):
    """Abstract base class for quantities computed in liquidlib"""

    def __init__(self, input_file="quantity.in"):
        """Constructor of class Quantity

        :param input_file: input file defining computation parameters
        """
        self.input_file = input_file
        self._input_checker = InputChecker()
        self._trajectory_factory = TrajectoryFactory()
        self._atom_selector = AtomSelector()

    def execute(self):
        """Executes all the procedures for calculation"""
        self._parse_input()
        self._check_input()
        self._read_trajectory()
        self._compute()
        self._write()

    def _parse_input(self):
        """Parses input parameters from input file"""
        self.input_parameters = InputParser.parse(self.input_file)  # parameters in a dict

    def _check_input(self):
        """Check the validity of input parameters """
        self._input_checker.check(self.input_parameters)

    def _read_trajectory(self):
        """Read trajectory

        Instantiate a trajectory class using simple factory pattern,
        then read trajectory content
        """
        # self.input_parameters = dict()
        # self.input_parameters["trajectory_file_name"] = "test.trr"
        trajectory_file_name = self.input_parameters["trajectory_file_name"]
        self.trajectory = self._trajectory_factory.create_trajectory(trajectory_file_name)
        self.trajectory.read(self.input_parameters)

    @abstractmethod
    def _compute(self):
        """Main logic to compute the quantity

        This method needs to be implemented in the derived class.
        """
        pass

    @abstractmethod
    def _write(self):
        """Write the result to a file

        This method needs to be implemented in the derived class.
        """
        pass

    @property
    def atom_selector(self):
        return self._atom_selector

    @atom_selector.setter
    def atom_selector(self, selector):
        self._atom_selector = selector

    @property
    def trajectory_factory(self):
        return self._trajectory_factory

    @trajectory_factory.setter
    def trajectory_factory(self, factory):
        self._trajectory_factory = factory

    @property
    def input_checker(self):
        return self._input_checker

    @input_checker.setter
    def input_checker(self, checker):
        self._input_checker = checker

    def __repr__(self):
        return "<class Quantity>: abstract base class for specific quantity."