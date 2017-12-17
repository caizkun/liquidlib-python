#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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

        :param input_parameters: a dictionary of input parameters
        :return: a boolean value indicating success (true) or failure (false)
        """
        pass


# --- Concrete Component ---

class GenericInputValidator(InputValidator):
    """
    Concrete class to check generic parameters for each calculation
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
    Decorator to validate parameters for real-space quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


class KSpaceDecorator(DecoratorOfInputValidator):
    """
    Decorator to validate parameters for reciprocal-space quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


class TDomainDecorator(DecoratorOfInputValidator):
    """
    Decorator to validate parameters for time-domain quantity
    """
    def __init__(self, input_validator):
        self.input_validator = input_validator

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)

        # add some specific checks

        pass


# --- decorated component for easy use in liquidlib ---

class RSpaceValidator(InputValidator):
    """
    Validate parameters for real-space quantity
    """
    def validate(self, input_parameters):
        input_validator = RSpaceDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class KSpaceValidator(InputValidator):
    """
    Validate parameters for reciprocal-space quantity
    """
    def validate(self, input_parameters):
        input_validator = KSpaceDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class TDomainValidator(InputValidator):
    """
    Validate parameters for time-domain quantity
    """
    def validate(self, input_parameters):
        input_validator = TDomainDecorator(GenericInputValidator())
        input_validator.validate(input_parameters)


class RSpaceTDomainValidator(InputValidator):
    """
    Validate parameters for the quantity in real-space and time-domain
    """
    def validate(self, input_parameters):
        input_validator = RSpaceDecorator(TDomainDecorator(GenericInputValidator()))
        input_validator.validate(input_parameters)


class KSpaceTDomainValidator(InputValidator):
    """
    Validate parameters for the quantity in reciprocal-space and time-domain
    """
    def validate(self, input_parameters):
        input_validator = KSpaceDecorator(TDomainDecorator(GenericInputValidator()))
        input_validator.validate(input_parameters)