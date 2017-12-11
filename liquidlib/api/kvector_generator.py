#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Classes for k-vectors generation
"""

class KvectorGenerator(object):
    """Base class of strategy to generate k-vector"""

    def __init__(self):
        pass

    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        """Abstract method to generate k-vectors

        This method needs to be implemented in the derived class
        """
        pass


class PermutationKevectorGenerator(KvectorGenerator):
    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        # define the strategy here
        pass


class RecursionKvectorGenerator(KvectorGenerator):
    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        # define the strategy here
        pass