#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Quantity
~~~~~~~~

Base class for the quantities computed in liquidlib.
"""

from abc import ABC, abstractmethod

from liquidlib.api.input_validator import GenericInputValidator, InputValidator

from liquidlib.api.atom_selector import AtomSelector
from liquidlib.api.input_parser import InputParser
from liquidlib.api.trajectory_factory import TrajectoryFactory


class Quantity(ABC):
    """
    Abstract base class for quantities computed in liquidlib
    """

    def __init__(self, input_file="quantity.in"):
        """Constructor of class Quantity

        :param input_file: input file defining the computation parameters
        """
        self.input_file = input_file
        self._input_validator = GenericInputValidator()
        self._trajectory_factory = TrajectoryFactory()
        self._atom_selector = AtomSelector()

    def execute(self):
        """Executes all the procedures for calculation"""
        self._parse_input()
        self._validate_input()
        self._read_trajectory()
        self._compute()
        self._write()

    def _parse_input(self):
        """Parses input parameters from input file"""
        self.input_parameters = InputParser.parse(self.input_file)  # parameters in a dict

    def _validate_input(self):
        """Check the validity of input parameters """
        self._input_validator.validate(self.input_parameters)

    def _read_trajectory(self):
        """Read trajectory

        Instantiate a trajectory class using simple factory pattern,
        then read the trajectory content
        """
        self.input_parameters = dict()
        self.input_parameters["trajectory_file_name"] = "test.trr"
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
    def trajectory_factory(self):
        return self._trajectory_factory

    @trajectory_factory.setter
    def trajectory_factory(self, factory):
        if not isinstance(factory, TrajectoryFactory):
            raise TypeError
        self._trajectory_factory = factory

    @property
    def input_validator(self):
        return self._input_validator

    @input_validator.setter
    def input_validator(self, validator):
        if not isinstance(validator, InputValidator):
            raise TypeError
        self._input_validator = validator

    @property
    def atom_selector(self):
        return self._atom_selector

    @atom_selector.setter
    def atom_selector(self, selector):
        if not isinstance(selector, AtomSelector):
            raise TypeError
        self._atom_selector = selector

    def __repr__(self):
        return "<class Quantity>: abstract base class for specific quantity."