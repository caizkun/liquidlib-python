#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Input Validator
~~~~~~~~~~~~~~~

Validate input parameters for the calculation
"""
# TODO: may throw exception


from abc import ABC, abstractmethod


class InputValidator(ABC):
    """
    Abstract base class for validating input parameters
    """
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, input_parameters):
        """
        Abstract method to validate input parameters
        """
        pass


# --- Concrete Component ---

class GenericInputValidator(InputValidator):
    """
    Class to check generic parameters for each calculation
    """
    def validate(self, input_parameters):
        """
        Validate generic parameters
        """

        # put generic checks here

        pass


# --- Decorator ---

class DecoratorOfInputValidator(InputValidator):
    """
    Abstract base decorator of input validators
    """
    pass


class RSpaceDecorator(DecoratorOfInputValidator):
    """
    Validate parameters for real-space quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


class KSpaceDecorator(DecoratorOfInputValidator):
    """
    Validate parameters for reciprocal-space quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


class TDomainDecorator(DecoratorOfInputValidator):
    """
    Validate parameters for time-domain quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


# --- decorated component for easy use in liquidlib ---

class RSpaceValidator(InputValidator):
    def validate(self, input_parameters):
        input_validator = RSpaceDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class KSpaceValidator(InputValidator):
    def validate(self, input_parameters):
        input_validator = KSpaceDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class TDomainValidator(InputValidator):
    def validate(self, input_parameters):
        input_validator = TDomainDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class RSpaceTDomainValidator(InputValidator):
    def validate(self, input_parameters):
        input_validator = RSpaceDecorator(TDomainDecorator(GenericInputValidator()))
        input_validator.validate(input_parameters)


class KSpaceTDomainValidator(InputValidator):
    def validate(self, input_parameters):
        input_validator = KSpaceDecorator(TDomainDecorator(GenericInputValidator()))
        input_validator.validate(input_parameters)