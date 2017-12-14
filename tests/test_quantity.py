#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from liquidlib.api.atom_selector import SelectByAtomId, AtomSelector
from liquidlib.api.input_validator import RSpaceValidator, InputValidator, RSpaceTDomainValidator, GenericInputValidator
from liquidlib.api.quantity import Quantity
from liquidlib.api.trajectory_factory import TrajectoryFactory, DemoTrajectoryFactory


class TestQuantity(unittest.TestCase):
    """
    Unit test cases for class Quantity
    """
    def setUp(self):
        class DerivedQuantity(Quantity):
            def _compute(self):
                pass

            def _write(self):
                pass

        self.cls = DerivedQuantity

    def tearDown(self):
        del self.cls

    def test_init_no_arg(self):
        quantity = self.cls()
        self.assertEqual(quantity.input_file, "quantity.in")

    def test_init_arg(self):
        filename = "derived_quantity.in"
        quantity = self.cls(filename)
        self.assertEqual(quantity.input_file, filename)

    def test_default_atom_selector(self):
        quantity = self.cls()
        self.assertIsInstance(quantity.atom_selector, AtomSelector)

    def test_set_correct_atom_selector(self):
        quantity = self.cls()
        quantity.atom_selector = SelectByAtomId()
        self.assertIsInstance(quantity.atom_selector, AtomSelector)
        self.assertIsInstance(quantity.atom_selector, SelectByAtomId)

    def test_set_wrong_atom_selector(self):
        quantity = self.cls()
        with self.assertRaises(TypeError):
            quantity.atom_selector = str()

    def test_default_input_validator(self):
        quantity = self.cls()
        self.assertIsInstance(quantity.input_validator, GenericInputValidator)

    def test_set_correct_input_validator(self):
        quantity = self.cls()
        quantity.input_validator = RSpaceValidator()
        self.assertIsInstance(quantity.input_validator, InputValidator)
        self.assertIsInstance(quantity.input_validator, RSpaceValidator)
        self.assertNotIsInstance(quantity.input_validator, RSpaceTDomainValidator)

    def test_set_wrong_input_validator(self):
        quantity = self.cls()
        with self.assertRaises(TypeError):
            quantity.input_validator = int()

    def test_default_trajectory_factory(self):
        quantity = self.cls()
        self.assertIsInstance(quantity.trajectory_factory, TrajectoryFactory)

    def test_set_correct_trajectory_factory(self):
        quantity = self.cls()
        quantity.trajectory_factory = DemoTrajectoryFactory()
        self.assertIsInstance(quantity.trajectory_factory, TrajectoryFactory)
        self.assertIsInstance(quantity.trajectory_factory, DemoTrajectoryFactory)

    def test_set_wrong_trajectory_factory(self):
        quantity = self.cls()
        with self.assertRaises(TypeError):
            quantity.trajectory_factory = self.cls()
