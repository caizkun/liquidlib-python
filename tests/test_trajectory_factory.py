#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from liquidlib.api.trajectory import XtcTrajectory
from liquidlib.api.trajectory_factory import TrajectoryFactory


class TestTrajectoryFactory(unittest.TestCase):
    """
    Unit test cases for class TrajectoryFactory
    """
    def setUp(self):
        self.trajectory_factory = TrajectoryFactory()

    def tearDown(self):
        del self.trajectory_factory

    def test_create_known_trajectory(self):
        trajectory = self.trajectory_factory.create_trajectory("traj.xtc")
        self.assertIsInstance(trajectory, XtcTrajectory)

    def test_create_unknown_trajectory(self):
        trajectory = self.trajectory_factory.create_trajectory("traj.random")
        self.assertEqual(trajectory, None)