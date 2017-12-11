#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classes for atom selection
"""


class AtomSelector(object):

    def __init__(self):
        pass

    def select(self, input_parameters, trajectory, **kwargs):
        """Abstract method to select atoms

        This method needs to be implemented in the derived class
        """
        # default selection strategy: SelectByAtomTypeAtomGroup
        pass


class SelectByAtomId(AtomSelector):
    def select(self, input_parameters, trajectory, **kwargs):
        # define a specific strategy here
        pass


class SelectByZDepth(AtomSelector):
    def select(self, input_parameters, trajectory, **kwargs):
        # define another specific strategy here
        pass
