#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Trajectory(object):
    """ This is a base class of trajectory. """
    def __init__(self):
        pass

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
        """ This method reads .trr file. """
        pass


class XtcTrajectory(Trajectory):
    def read(self, input_parameters):
        """ This method reads .xtc file. """
        pass


class XyzTrajectory(Trajectory):
    def read(self, input_parameters):
        """ This method reads .xyz file. """
        pass


class LammpsTrajectory(Trajectory):
    def read(self, input_parameters):
        """ This method reads .lammpstrj file. """
        pass