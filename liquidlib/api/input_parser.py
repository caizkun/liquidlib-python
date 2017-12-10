#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
        except:
            print("Incorrect input format encountered!")
            print("Note that errors may arise in the calculation \
                    if some parameters are missing.")
            # exit(-1)
        finally:
            # close the file and maybe clean up
            pass

        return parameters