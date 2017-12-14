#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classes for atom selection
"""


class AtomSelector(object):
    """
    Base class for atom selection
    """

    def __init__(self):
        pass

    def select(self, input_parameters, trajectory, **kwargs):
        # default selection strategy
        pass


class SelectByAtomId(AtomSelector):
    def select(self, input_parameters, trajectory, **kwargs):
        # define a specific strategy here
        pass


class SelectByZDepth(AtomSelector):
    def select(self, input_parameters, trajectory, **kwargs):
        # define another specific strategy here
        pass
