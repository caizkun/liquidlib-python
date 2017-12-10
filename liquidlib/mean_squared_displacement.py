#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from liquidlib.api.input_validator import TDomainValidator
from liquidlib.api.quantity import Quantity


# class MeanSquaredDisplacementValidator(TDomainValidator):
#     def validate(self, input_parameters):
#         super().validate(input_parameters)
#         # add specific checks for the quantity if necessary


class MeanSquaredDisplacement(Quantity):
    """
    Mean Squared Displacement
    """
    def __init__(self, input_file="r2_t.in"):
        """
        Constructor

        :param input_file: input file defining the computation parameters
        """
        super().__init__(input_file)
        self._input_validator = TDomainValidator()

    def _compute(self):
        """
        Main logic to compute the quantity
        """
        selected_atom_indexes = self._atom_selector.select(self.input_parameters, self.trajectory)

        # implement the headache logic here

        pass

    def _write(self):
        """
        Write the result to a file
        """
        pass

    def __repr__(self):
        return "<class MeanSquaredDisplacement>"


def main():
    """
    Compute the mean squared displacement
    """
    input_file = "r2_t.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])

    mean_squared_displacement = MeanSquaredDisplacement(input_file)

    print(mean_squared_displacement.input_file)
    print("%r" % mean_squared_displacement)

    # Below demonstrate a few more customizations available if needed.
    # If these customizations still do not fit your needs, you may consider
    # inheriting the specific quantity your are interested in, and override
    # some of the methods.

    # if using a new strategy to select atoms
    # mean_squared_displacement.atom_selector = SelectByAtomId()

    # if validating new parameters provided in the input file
    # mean_squared_displacement.input_validator = DemoMeanSquaredDisplacementInputValidator()

    # if reading a new uncommon trajectory type
    # mean_squared_displacement.trajectory_factory = DemoTrajectoryFactory()

    mean_squared_displacement.execute()


if __name__ == '__main__':
    main()

