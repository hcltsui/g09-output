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
        
        directory: directory containing the files, exclude "\\", 
            default="polar-extra\\"        
        """
        onedrive = "D:\\OneDrive - Newcastle University\\"
        g09_dir = onedrive+"python scripts\\gaussian09\\"
        sub_dir = g09_dir+"polar-extract\\"+directory+"\\"
        self.dipole_input = pd.read_csv(sub_dir+"dipole-input.csv",index_col=0)
        self.dipole_dipole = pd.read_csv(sub_dir+"dipole-dipole.csv",index_col=0)
        self.dipole = pd.concat([self.dipole_input,self.dipole_dipole],
                                axis=1,keys=["input","dipole"])
        self.alpha_input = pd.read_csv(sub_dir+"alpha-input.csv",index_col=0)
        self.alpha_dipole = pd.read_csv(sub_dir+"alpha-dipole.csv",index_col=0)
        self.alpha = pd.concat([self.alpha_input,self.alpha_dipole],
                               axis=1,keys=["input","dipole"])
        self.beta_input = pd.read_csv(sub_dir+"beta-input.csv",index_col=0)
        self.beta_dipole = pd.read_csv(sub_dir+"beta-dipole.csv",index_col=0)
        self.beta = pd.concat([self.beta_input,self.beta_dipole],
                              axis=1,keys=["input","dipole"])
        self.gamma_input = pd.read_csv(sub_dir+"gamma-input.csv",index_col=0)
        self.gamma_dipole = pd.read_csv(sub_dir+"gamma-dipole.csv",index_col=0)
        self.gamma = pd.concat([self.gamma_input,self.gamma_dipole],
                               axis=1,keys=["input","dipole"])

class Display:
    """Display function for polar data from dataframe"""
    def gamma(molecule_df,components):
        """Display Gamma values of components of a molecule. 
        
        Parameters
        ----------
        molecule_df: dataframe object generated from Polar_df
        compoents: list, components to be displayed        
        """
        for com in components:
            print(com)
            print("Gamma(-w;w,0)")
            print("input - 530nm: {}, 1060nm: {}; ".format(molecule_df.gamma["input"]["Gamma(-w;w0) w=530nm"][com],
                                                           molecule_df.gamma["input"]["Gamma(-w;w0) w=1060nm"][com])+\
                  "dipole - 530nm: {}, 1060nm: {}".format(molecule_df.gamma["dipole"]["Gamma(-w;w0) w=530nm"][com],
                                                          molecule_df.gamma["dipole"]["Gamma(-w;w0) w=1060nm"][com]))
            print("Gamma (-2w;w,w)")
            print("input - 530nm: {}, 1060nm: {}; ".format(molecule_df.gamma["input"]["Gamma(-2w;ww) w=530nm"][com],
                                                           molecule_df.gamma["input"]["Gamma(-2w;ww) w=1060nm"][com])+\
                  "dipole - 530nm: {}, 1060nm: {}".format(molecule_df.gamma["dipole"]["Gamma(-2w;ww) w=530nm"][com],
                                                          molecule_df.gamma["dipole"]["Gamma(-2w;ww) w=1060nm"][com]))                
                