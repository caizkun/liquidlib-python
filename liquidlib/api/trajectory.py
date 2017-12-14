#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TrajectoryFactory
~~~~~~~~

A simple factory to create trajectory of specific types
"""

from abc import ABC, abstractmethod


class Trajectory(ABC):
    """
    Abstract base class of trajectory
    """
    def __init__(self):
        pass

    @abstractmethod
    def read(self, input_parameters):
        """
        Read trajectory from the trajectory file

        :param input_parameters:
        :return:
        """
        pass

    def wrap_coordinates(self):
        """
        Wrap the coordinates (reinforce the periodic boundary condition)
        """
        pass

    def unwrap_coordinates(self):
        """
        Unwrap the coordinates (periodic boundary condition removed)
        """
        pass

    def compute_velocities(self):
        """
        Compute velocities from the coordinates
        """
        pass


class TrrTrajectory(Trajectory):
    def read(self, input_parameters):
        """
        Read .trr file
        """
        pass


class XtcTrajectory(Trajectory):
    def read(self, input_parameters):
        """
        Read .xtc file
        """
        pass


class XyzTrajectory(Trajectory):
    def read(self, input_parameters):
        """
        Read .xyz file
        """
        pass


class LammpsTrajectory(Trajectory):
    def read(self, input_parameters):
        """
        Read .lammpstrj file
        """
        pass


class PdbTrajectory(Trajectory):
    def read(self, input_parameters):
        """
        Read .pdb file
        """
        pass