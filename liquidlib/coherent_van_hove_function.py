#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Coherent Van Hove Function
"""

import sys

from liquidlib.api.input_validator import RSpaceTDomainValidator
from liquidlib.api.quantity import Quantity


# class CoherentVanHoveFunctionValidator(RSpaceTDomainValidator):
#     def validate(self, input_parameters):
#         super().validate(input_parameters)
#         # add specific checks for the quantity if necessary


class CoherentVanHoveFunction(Quantity):
    def __init__(self, input_file="G_rt.in"):
        super().__init__(input_file)
        self._input_validator = RSpaceTDomainValidator()

    def _compute(self):
        selected_atom_indexes = self._atom_selector.select(self.input_parameters, self.trajectory)
        # ---------------------------------
        # implement the headache logic here
        # ---------------------------------
        pass

    def _write(self):
        pass

    def __repr__(self):
        return "<class CoherentVanHoveFunction> instantiated from input file '%s'" % self.input_file


def main():
    input_file = "G_rt.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])

    coherent_van_hove_function = CoherentVanHoveFunction(input_file)

    print(coherent_van_hove_function.input_file)
    print("%r" % coherent_van_hove_function)

    # Below demonstrate a few more customizations available if needed.
    # If these customizations still do not fit your needs, you may consider
    # inheriting the specific quantity your are interested in, and override
    # some of the methods.

    # if using a new strategy to select atoms
    # coherent_van_hove_function.atom_selector = YourAtomSelector()

    # if using a new input validator to validate new parameters in the input file
    # coherent_van_hove_function.input_validator = YourInputValidator()

    # if using a new trajectory factory to create a new uncommon trajectory type
    # coherent_van_hove_function.trajectory_factory = YourTrajectoryFactory()

    coherent_van_hove_function.execute()


if __name__ == '__main__':
    main()
