"""
PhysicalQuantity
~~~~~~~~~~~~~~~~

This is the base class for the physical quantities computed in liquidlib.

"""


class PhysicalQuantity(object):
    """ Base class for physical quantities computed in liquidlib """

    def __init__(self):
        pass

    def execute(self, input_file="quantity.in"):
        self._parse_input(input_file)
        self._read_trajectory()
        self._compute()
        self._write()

    def _parse_input(self, input_file="quantity.in"):
        self.input_file = input_file
        self.input_parser = InputParser()
        self.input_parameters = self.input_parser.parse(self.input_file)

    def _read_trajectory(self):
        self.trajectoryFactory = TrajectoryFactory(self.input_parameters["trajectory_file_name"])
        self.trajectory = self.trajectoryFactory.prepareTrajectory(self.input_parameters)

    def _compute(self):
        pass

    def _write(self):
        pass

    def __repr__(self):
        return "<class PhysicalQuantity>: the base class for specific quantities."