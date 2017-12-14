#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
TrajectoryFactory
~~~~~~~~

A simple factory to create trajectory
"""

from liquidlib.api.trajectory import TrrTrajectory, XtcTrajectory, XyzTrajectory, LammpsTrajectory, PdbTrajectory


class TrajectoryFactory(object):
    """A simple factory to prepare trajectory"""

    def __init__(self):
        pass

    def create_trajectory(self, trajectory_file_name):
        """Returns a specific trajectory type based on the file type

        :param trajectory_file_name: file name of the trajectory file
        """
        trajectory_file_type = str(trajectory_file_name).split(".")[-1]

        if trajectory_file_type == "trr":
            return TrrTrajectory()
        elif trajectory_file_type == "xtc":
            return XtcTrajectory()
        elif trajectory_file_type == "xyz":
            return XyzTrajectory()
        elif trajectory_file_type == "lammpstrj":
            return LammpsTrajectory()

        return None


class DemoTrajectoryFactory(TrajectoryFactory):
    """A demo class to extend TrajectoryFactory"""

    def prepare_trajectory(self, trajectory_file_name):
        trajectory = super().create_trajectory(trajectory_file_name)

        if trajectory is None:
            trajectory_file_type = str(trajectory_file_name).split(".")[-1]

            if trajectory_file_type == ".pdb":
                trajectory = PdbTrajectory()

        return trajectory