#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write the output to file
"""

class OutputWriter(object):
    """
    Utility class to write the output to file
    """

    def __init__(self):
        pass

    @staticmethod
    def write1D(filename, x, fx, header=None):
        """
        Write 1D data to a file

        :param filename: name of output file
        :param x: a list of variable values
        :param fx: a list of results, forming pairs of (x, fx)
        :param header: header to print in the top of output file
        """
        pass

    @staticmethod
    def write2D(filename, x, y, fxy, header=None):
        """
        Write 2D data to a file

        :param filename: name of output file
        :param x: a list of values of the 1st variable,
                  which would be printed in a single column in the output file
        :param y: a list of values of the end variable,
                  which would be printed in a column aligned with the columns of fxy
        :param fx: a list of results, forming pairs of (y, fx1y, fx2y, ...)
        :param header: header to print in the top of output file
        """
        pass