#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InputValidator(object):
    """
    Base class for validating input parameters
    """
    def __init__(self):
        pass

    def validate(self, input_parameters):
        """
        Validate generic parameters
        """
        pass


# TODO: use decorator to add more checking points
# TODO: may throw exception


class RDomainQuantityValidator(InputValidator):
    """
    Check parameters for real space quantity
    """
    def validate(self, input_parameters):
        pass


class KDomainQuantityValidator(InputValidator):
    """
    Check parameters for reciprocal space quantity
    """
    def validate(self, input_parameters):
        pass


class TDomainQuantityValidator(InputValidator):
    """
    Check parameters for time domain quantity
    """
    def validate(self, input_parameters):
        pass


class InputValidatorDecorator(InputValidator):
    """
    Base decorator class of input validator
    """
    pass


class RTDomainQuantityValidator(InputValidator):
    """
    Concrete decorator class of input validator
    """
    def validate(self, input_parameters):
        input_validator = RDomainQuantityValidator()
        input_validator.validate(input_parameters)
        input_validator = TDomainQuantityValidator()
        input_validator.validate(input_parameters)


class KTDomainQuantityValidator(InputValidator):
    """
    Concrete decorator class of input validator
    """
    def __init__(self):
        self.input_validator = InputValidator()

    def validate(self, input_parameters):
        self.input_validator.validate(input_parameters)
