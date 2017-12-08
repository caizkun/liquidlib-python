#!/usr/bin/env python
# -*- coding: utf-8 -*-


class InputChecker(object):
    """ Check input parameters """
    def __init__(self):
        pass

    def check(self, input_parameters):
        """ check generic parameters """
        pass


# TODO: use decorator to add more checking points
# TODO: may throw exception

class RDomainInputChecker(InputChecker):
    """ Check parameters for real space quantity """
    def check(self, input_parameters):
        super().check(input_parameters)
        # add
        pass


class KDomainInputChecker(InputChecker):
    pass


class RTDomainInputChecker(InputChecker):
    pass


class KTDomainInputChecker(InputChecker):
    pass

