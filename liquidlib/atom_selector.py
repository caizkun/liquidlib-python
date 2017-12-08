#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AtomSelector(object):
    """Class for atom selection"""

    def __init__(self):
        """Constructor of AtomSelector class"""
        self._selection_strategy = SelectionStrategy()

    @property
    def selection_strategy(self):
        """Get selection strategy"""
        return self._selection_strategy

    @selection_strategy.setter
    def selection_strategy(self, strategy):
        """Set selection strategy"""
        self._selection_strategy = strategy

    def select_atoms(self, system_atom_list, atom_types, atom_group, **kwargs):
        """
        Public interface to select atoms

        :param system_atom_list:
        :param atom_types:
        :param atom_group:
        :param kwargs:
        :return:
        """
        return self.selection_strategy.select(system_atom_list, atom_types, atom_group, **kwargs)


class SelectionStrategy(object):

    def __init__(self):
        pass

    def select(self, system_atom_list, atom_types, atom_group, **kwargs):
        """Abstract method to select atoms

        This method needs to be implemented in the derived class
        """
        pass


class SelectByAtomId(SelectionStrategy):
    def select(self, system_atom_list, atom_types, atom_group, **kwargs):
        # define a specific strategy here
        pass


class SelectByZDepth(SelectionStrategy):
    def select(self, system_atom_list, atom_types, atom_group, **kwargs):
        # define another specific strategy here
        pass
