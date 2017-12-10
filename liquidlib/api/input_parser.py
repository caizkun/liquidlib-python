#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import traceback


class InputParser(object):
    """ Input file parser

    return: a dictionary of input parameters
    """

    def __init__(self):
        pass

    @staticmethod
    def parse(input_file):
        """
        Parse the input file to retrieve input parameters

        :param input_file: input file defining the computation parameters
        :return: a dictionary of input parameters
        """
        # TODO: is json or xml more suitable for the input file format?
        parameters = dict()

        try:
            # open and parse the file
            pass
        except FileNotFoundError:
            print("Input file '%s' not found" % input_file)
            sys.exit(-1)
        except:
            print("Unexpected error!")
            traceback.print_exc()
            sys.exit(-1)
        finally:
            # close the file and maybe clean up
            pass

        return parameters