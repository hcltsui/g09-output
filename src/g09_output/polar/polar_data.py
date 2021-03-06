# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 14:02:17 2022

@author: hclts
"""

import pandas as pd

class Polar_df:
    """Extracted data from polar output and generates pandas dataframe.
    
    Attributes
    ----------
    directory: the sub-directory name containing the csv files
    """
    def __init__(self,directory):
        """Generate dataframe for dipole, alpha, beta and gamma.
        
        directory: directory containing the files, exclude "\\"       
        """
        data_dir = directory+"\\"
        self.dipole_input = pd.read_csv(data_dir+"dipole-input.csv",index_col=0)
        self.dipole_dipole = pd.read_csv(data_dir+"dipole-dipole.csv",index_col=0)
        self.dipole = pd.concat([self.dipole_input,self.dipole_dipole],
                                axis=1,keys=["input","dipole"])
        self.alpha_input = pd.read_csv(data_dir+"alpha-input.csv",index_col=0)
        self.alpha_dipole = pd.read_csv(data_dir+"alpha-dipole.csv",index_col=0)
        self.alpha = pd.concat([self.alpha_input,self.alpha_dipole],
                               axis=1,keys=["input","dipole"])
        self.beta_input = pd.read_csv(data_dir+"beta-input.csv",index_col=0)
        self.beta_dipole = pd.read_csv(data_dir+"beta-dipole.csv",index_col=0)
        self.beta = pd.concat([self.beta_input,self.beta_dipole],
                              axis=1,keys=["input","dipole"])
        self.gamma_input = pd.read_csv(data_dir+"gamma-input.csv",index_col=0)
        self.gamma_dipole = pd.read_csv(data_dir+"gamma-dipole.csv",index_col=0)
        self.gamma = pd.concat([self.gamma_input,self.gamma_dipole],
                               axis=1,keys=["input","dipole"])

        
                