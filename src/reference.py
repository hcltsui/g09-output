# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 15:49:04 2022

@author: hclts
"""

from numpy import genfromtxt

periodic_table = genfromtxt("periodic_table.csv",
                            dtype=str,delimiter=",",skip_header=1)