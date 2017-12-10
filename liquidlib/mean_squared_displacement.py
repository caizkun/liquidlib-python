#!/usr/bin/env python
# -*- coding: utf-8 -*-
from liquidlib.api.input_validator import TDomainQuantityValidator
from liquidlib.api.quantity import Quantity


class MeanSquaredDisplacementInputChecker(TDomainQuantityValidator):
    pass


class MeanSquaredDisplacement(Quantity):
    """
    Mean Squared Displacement
    """

    def __init__(self, input_file="r2_t.in"):
        """
        Constructor of PairDistributionFunction class

        :param input_file: input file defining the computation parameters
        """
        super().__init__(input_file)
        self.input_checker = MeanSquaredDisplacementInputChecker()

    def _compute(self):
        """
        Main logic to compute the quantity
        """
        # do the heavy lifting here
        pass

    def _write(self):
        """
        Write the result to a file
        """
        # TODO: may use a Util class
        pass

    def __repr__(self):
        return "<class MeanSquaredDisplacement>"



