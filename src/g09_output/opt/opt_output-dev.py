# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:30:57 2022

@author: nht45
"""

import numpy as np

directory = "MAPbBr3-2\\Pb-Br\\opt-2\\"
filename = "MAPbBr3-PbBr-opt-1-pm6-1"

onedrive = "D:\\OneDrive - Newcastle University\\"
g09_dir = onedrive+"hpc\\gaussian09\\"
sub_dir = g09_dir+directory
filename = filename
fname = sub_dir+filename+".out"

f = open(fname,"r")
lines = f.readlines()
f.close()

breakline = " ---------------------------------------------------------------------"

header_index = []
breakline_index = []
for num,line in enumerate(lines):
    if "Standard orientation:" in line:
        header_index.append(num)
    if breakline in line:
        breakline_index.append(num)

# print(header_index[-1])
section_start_ind = header_index[-1]
coord_section_index = []
for i in breakline_index:
    if i > section_start_ind+3:
        coord_section_index.append(i)

coord_section_start = coord_section_index[0]+1
coord_section_end = coord_section_index[1]
atom_num = coord_section_end-coord_section_start
coord_section = lines[coord_section_start:coord_section_end]
# print(coord_section)


atom_line = coord_section[-1]
atom_line = atom_line.replace("\n","")
atom_line_split = atom_line.split(" ")
# print(atom_line_split)
atom_line_new = []
for i in atom_line_split:
    if i != "":
        atom_line_new.append(i)
print(atom_line_new)

centre_num = atom_line_new[0]
atomic_num = atom_line_new[1]
atomic_type = atom_line_new[2]
coord_x = atom_line_new[3]
coord_y = atom_line_new[4]
coord_z = atom_line_new[5]

periodic_table = np.genfromtxt("periodic_table.csv",delimiter=",",dtype=str,skip_header=1)
for i in periodic_table:
    if atomic_num  == i[0]:
        element = i[1]
        break



xyz_header = "{}\n{}\n".format(atom_num,filename)
xyz_line = "{}{} {} {} {}\n".format(element,centre_num,coord_x,coord_y,coord_z)
with open("{}.xyz".format(filename),"w") as f:
    f.writelines(xyz_header)
    f.writelines(xyz_line)
