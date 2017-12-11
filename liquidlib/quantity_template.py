#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A template for writing a NEW quantity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Note:
To write a specific version of an existing quantity, consider inheriting the class
of that quantity.

Usage:
1. Execute the below command in terminal to replace the name for class and variable
    $ copy quantity_template.py your_quantity_filename.py
    $ sed -i.bak 's/TemplateQuantity/YourClassName/g' your_quantity_filename.py
    $ sed -i.bak 's/template_quantity/your_quantity_variable/g' your_quantity_filename.py

2. Now it is your turn to code the main logic for the quantity.
"""

import sys

from liquidlib.api.input_validator import InputValidator
from liquidlib.api.quantity import Quantity


class TemplateQuantityValidator(InputValidator):
    def validate(self, input_parameters):
        pass


class TemplateQuantity(Quantity):
    def __init__(self, input_file="template_quantity.in"):
        super().__init__(input_file)
        self._input_validator = TemplateQuantityValidator()

    def _compute(self):
        selected_atom_indexes = self._atom_selector.select(self.input_parameters, self.trajectory)
        # ---------------------------------
        # implement the headache logic here
        # ---------------------------------
        pass

    def _write(self):
        pass

    def __repr__(self):
        return "<class TemplateQuantity> instantiated from input file '%s'" % self.input_file


def main():
    input_file = "template_quantity.in"
    if len(sys.argv) > 1:
        input_file = str(sys.argv[1])

    template_quantity = TemplateQuantity(input_file)

    print(template_quantity.input_file)
    print("%r" % template_quantity)

    # Below demonstrate a few more customizations available if needed.
    # If these customizations still do not fit your needs, you may consider
    # inheriting the specific quantity your are interested in, and override
    # some of the methods.

    # if using a new strategy to select atoms
    # template_quantity.atom_selector = YourAtomSelector()

    # if using a new input validator to validate new parameters in the input file
    # template_quantity.input_validator = YourInputValidator()

    # if using a new trajectory factory to create a new uncommon trajectory type
    # template_quantity.trajectory_factory = YourTrajectoryFactory()

    template_quantity.execute()


if __name__ == '__main__':
    main()