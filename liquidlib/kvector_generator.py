#!/usr/bin/env python
# -*- coding: utf-8 -*-


class KvectorGenerator(object):
    """ Class for k-vectors generation """

    def __init__(self):
        self._generation_strategy = GenerationStrategy()

    @property
    def generation_strategy(self):
        """Get generation strategy"""
        return self._generation_strategy

    @generation_strategy.setter
    def generation_strategy(self, strategy):
        """Set generation strategy"""
        # TODO: check if correct class type
        self._generation_strategy = strategy

    def generate_kvectors(self, kvalue, dimension=3, max_kvec_num=100, **kwargs):
        """
        Public interface to generate k-vectors

        :param kvalue:
        :param dimension:
        :param max_kvec_num:
        :param kwargs:
        :return: 
        """
        return self._generation_strategy.generate(kvalue, dimension=3, max_kvec_num=100, **kwargs)


class GenerationStrategy(object):
    """Base class of strategy to generate k-vector"""

    def __init__(self):
        pass

    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        """Abstract method to generate k-vectors

        This method needs to be implemented in the derived class
        """
        pass


class PermutationStrategy(GenerationStrategy):
    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        # define the strategy here
        pass


class RecursionStrategy(GenerationStrategy):
    def generate(self, kvalue, max_kvec_num=100, **kwargs):
        # define the strategy here
        pass