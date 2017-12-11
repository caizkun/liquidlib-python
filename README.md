# liquidlib-python

A reconstructed, mini-skeleton of [LiquidLib](http://zhang-group.github.io/LiquidLib/) written in Python

Liquidlib is a post-processing package for molecular simulations written in C++. It takes a trajectory (containing atomic coordinates, etc.) output from simulation, and compute some physical quantities as instructed by a input file, which defines all the necessary parameters for the calculation.

This repos is one of my attempts to apply design patterns to some problems we have worked on before. I am pretty sure there are still a few places that can be improved. The code may not be that *Pythonic* as we may need to rewrite the C++ version if it works. So the code is more like a demo.  


**Design patterns applied**:
* *Simple factory*: to instantiate trajectory of specific type
* *Strategy*: to select atoms of interest
* *Decorator*: to validate inputs based on variable dependency   


**Useful references**:
* [Head First Design Pattern](http://shop.oreilly.com/product/9780596007126.do)
* [OODesign](http://www.oodesign.com/)
* [Design Patterns (Gof4)](https://sourcemaking.com/design_patterns)
* [faif/python-patterns](https://github.com/faif/python-patterns)
