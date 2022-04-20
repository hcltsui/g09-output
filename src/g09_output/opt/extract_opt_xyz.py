# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:01:55 2022

@author: hclts
"""

from g09_output import Opt

molecule = Opt("MDNBr\\opt-1\\","MDNBr-opt-1-pm6-1-1")
molecule.get_xyz()