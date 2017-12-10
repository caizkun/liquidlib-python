#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Trajectory(ABC):
    """ This is a base class of trajectory. """
    def __init__(self):
        pass

    @abstractmethod
    def read(self, input_parameters):
        pass

    def wrap_coordinates(self):
        pass

    def unwrap_coordinates(self):
        pass

    def compute_velocities(self):
        pass


class TrrTrajectory(Trajectory):
    def read(self, input_parameters):
        """Read .trr file"""
        pass


class XtcTrajectory(Trajectory):
    def read(self, input_parameters):
        """Read .xtc file"""
        pass


class XyzTrajectory(Trajectory):
    def read(self, input_parameters):
        """Read .xyz file"""
        pass


class LammpsTrajectory(Trajectory):
    def read(self, input_parameters):
        """Read .lammpstrj file """
        pass


class PdbTrajectory(Trajectory):
    def read(self, input_parameters):
        """Read .pdb file"""
        pass