#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Coherent Intermediate Scattering Function
"""

import sys

from liquidlib.api.input_validator import KSpaceTDomainValidator
from liquidlib.api.quantity import Quantity


# class CoherentIntermediateScatteringValidator(KSpaceTDomainValidator):
#     def validate(self, input_parameters):
#         super().validate(input_parameters)
#         # add specific checks for the quantity if necessary


class CoherentIntermediateScattering(Quantity):
    """
    Coherent Intermediate Scattering Function
    """
    def __init__(self, input_file="G_rt.in"):
        """
        Constructor

        :param input_file: input file defining the computation parameters
        """
        super().__init__(input_file)
        self._input_validator = KSpaceTDomainValidator()

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
        pass

    def __repr__(self):
        return "<class CoherentIntermediateScattering> instantiated from input file '%s'" % self.input_file


def main():
    """
    Compute the mean squared displacement
    """
    input_file = "F_kt.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])

    coherent_intermediate_scattering = CoherentIntermediateScattering(input_file)

    print(coherent_intermediate_scattering.input_file)
    print("%r" % coherent_intermediate_scattering)

    # Below demonstrate a few more customizations available if needed.
    # If these customizations still do not fit your needs, you may consider
    # inheriting the specific quantity your are interested in, and override
    # some of the methods.

    # if using a new strategy to select atoms
    # coherent_intermediate_scattering.atom_selector = SelectByAtomId()

    # if validating new parameters provided in the input file
    # coherent_intermediate_scattering.input_validator = DemoCoherentIntermediateScatteringValidator()

    # if reading a new uncommon trajectory type
    # coherent_intermediate_scattering.trajectory_factory = DemoTrajectoryFactory()

    coherent_intermediate_scattering.execute()


if __name__ == '__main__':
    main()

