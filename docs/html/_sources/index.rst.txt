.. liquidlib-python documentation master file, created by
   sphinx-quickstart on Mon Dec 11 16:27:43 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to liquidlib-python's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Liquidlib-python presents a reconstructed mini-skeleton of `LiquidLib <http://zhang-group.github.io/LiquidLib/>`_ in Python.

Liquidlib is a post-processing package for molecular simulations written in C++. It takes a trajectory (containing atomic coordinates, etc.) output from simulation, and compute some physical quantities as instructed by an input file, which defines all the necessary parameters for the calculation.

This repo is my attempt to apply design patterns to reconstruct LiquidLib. The code is more like a demo and many code blocks that implment the main algorithms have been skipped.



**Indices and tables**

* :ref:`modindex`
* :ref:`genindex`


**Design patterns applied**:

- *Simple factory pattern*: to instantiate a trajectory of specific type
- *Strategy pattern*: to select atoms of interest
- *Decorator pattern*: to validate inputs based on variable dependency


**Useful references**:

- `OODesign <http://www.oodesign.com/>`_
- `Head First Design Pattern <http://shop.oreilly.com/product/9780596007126.do>`_
- `Design Patterns (Gof4) <https://sourcemaking.com/design_patterns>`_
