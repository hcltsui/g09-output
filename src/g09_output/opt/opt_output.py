# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 13:06:57 2022

@author: nht45
"""

class Opt:
    """A class for extracting xyz coordinates from gaussian09 Polar output
    
    Attributes
    ----------
    filename: assume file extension = ".out"; no "." in filename
    
    Methods
    -------
    get_xyz() 
        Generates xyz files in the same directory as output file.
    """
    def __init__(self,filename):
        self.fname = filename
        
    def _check_optimised(self,lines):
        """Check if optimisation is completed. """
        optimised = False
        optimised_line = " Optimization completed."
        for line in lines:
            if optimised_line in line:
                optimised = True
                break
        return optimised
    
    def _get_section(self,lines):
        """Return the start and end index for the optimised coordination section."""
        breakline = " ---------------------------------------------------------------------"
        header_index = []
        breakline_index = []
        for num,line in enumerate(lines):
            if "Standard orientation:" in line:
                header_index.append(num)
            if breakline in line:
                breakline_index.append(num)
        # identify coordination section
        start_index = header_index[-1]+5
        for i in breakline_index:
            if i > start_index:
                end_index = i
                break
        return (start_index,end_index)
    
    def _get_coord(self,section):
        """Return list of elements and coordinates."""
        atom_list = []
        atom_coord_list = []
        for line in section:
            line = line.replace("\n","")
            line = line.split(" ")
            atom = {}
            newline = []
            for string in line:
                if string != "":
                    newline.append(string)
            atom["centre_num"] = newline[0]
            atom["atomic_num"] = newline[1]
            atom["atomic_type"] = newline[2]
            atom["x"] = newline[3]
            atom["y"] = newline[4]
            atom["z"] = newline[5]
            # convert atomic number to element symbol
            atomic_number = atom["atomic_num"]
            symbol = self._get_symbol(atomic_number)
            atom["symbol"] = symbol
            atom_list.append(atom)
            atom_coord = "{}{} {} {} {}".format(atom["symbol"],
                                                atom["centre_num"],
                                                atom["x"],atom["y"],atom["z"])
            atom_coord_list.append(atom_coord)
        return atom_coord_list
        
    def _get_symbol(self,atomic_num):
        """Return symbol from periodic table."""
        from numpy import genfromtxt
        import g09_output.opt as opt_module
        data_dir = opt_module.__path__[0]+"\\"
        periodic_table = genfromtxt(data_dir+"periodic_table.csv",
                                    dtype=str,delimiter=",",skip_header=1)
        for element in periodic_table:
            if atomic_num  == element[0]:
                symbol = element[1]
                break
        return symbol
    
    def _export_xyz(self,atom_coord_list):
        """Export xyz file."""
        num = len(atom_coord_list)
        fname = self.fname.split(".")[0]+".xyz"
        xyz_header = "{}\n{}\n".format(num,self.fname)
        with open(fname,"w") as f:
            f.writelines(xyz_header)
            print(xyz_header)
            for i in atom_coord_list:
                f.writelines("{}\n".format(i))
                print("{}".format(i))
                
    def get_xyz(self):
        """Export coordinate in xyz file in the same directory as output file."""
        f = open(self.fname,"r")
        lines = f.readlines()
        f.close()
        
        optimised = self._check_optimised(lines)
        if optimised == True:
            section_index = self._get_section(lines)
            section = lines[section_index[0]:section_index[1]]
            atom_coord_list = self._get_coord(section)
            self._export_xyz(atom_coord_list)
            print("DONE.")
        elif optimised == False:
            print("WARNING: Optimization is not completed.")
            pass