#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AtomSelector(object):

    def __init__(self, input_parameters):
        pass

    def select(self):
        """Abstract method to select atoms

        This method needs to be implemented in the derived class
        """
        # default selection strategy
        pass


class SelectByAtomTypeAtomGroup(AtomSelector):
    def select(self):
        pass


class SelectByAtomId(AtomSelector):
    def __init__(self):
        # add helper variables
        pass

    def select(self):
        # define a specific strategy here
        pass


class SelectByZDepth(AtomSelector):
    def select(self):
        # define another specific strategy here
        pass
