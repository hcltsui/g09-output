# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:02:21 2022

@author: hclts
"""

import numpy as np
import pathlib
# pathlib.Path("..\\polar-extract\\MDNB").mkdir(exist_ok=True)

onedrive = "D:\\OneDrive - Newcastle University\\"
g09_dir = onedrive+"hpc\\gaussian09\\"
sub_dir = g09_dir+"MDNBr-NH4Br6\\b3lyp\\3-21g-1\\"
filename = "MDNBr-NH4Br6-b3lyp-321g"
fname = sub_dir+filename+".out"

f = open(fname,"r")
lines = f.readlines()
f.close()

dipole_start = " Electric dipole moment"
dipole_end = "   z       "
dipole_start_i = []
dipole_end_i = []
alpha_start = " Dipole polarizability, Alpha"
alpha_end = "   zz       "
alpha_start_i = []
alpha_end_i = []
beta_start = " First dipole hyperpolarizability, Beta"
beta_end = "   zzz       "
beta_start_i = []
beta_end_i = []
gamma_start = " Second dipole hyperpolarizability, Gamma "
gamma_end = "   zzzz       "
gamma_start_i = []
gamma_end_i = []


for i,val in enumerate(lines):
    if dipole_start in val:
        dipole_start_i.append(i)
    if dipole_end in val:
        dipole_end_i.append(i)
    if alpha_start in val:
        alpha_start_i.append(i)
    if alpha_end in val:
        alpha_end_i.append(i)
    if beta_start in val:
        beta_start_i.append(i)
    if beta_end in val:
        beta_end_i.append(i)
    if gamma_start in val:
        gamma_start_i.append(i)
    if gamma_end in val:
        gamma_end_i.append(i)


def convert_char(line):
    space9 = "         "
    space8 = "        "
    space6 = "      "
    space3 = "   "
    space2 = "  "
    space1 = " "
    space0 = ""
    parallel = "|| "
    perpend = "_|_"
    if parallel in line:
        line = line.replace(parallel,"parallel")
    if perpend in line:
        line = line.replace(perpend,"perpendicular")
    if space9 in line:
        line = line.replace(space9,space1)
    if space8 in line:
        line = line.replace(space8,space1)
    if space6 in line:
        line = line.replace(space6,space1)
    if space3 in line:
        line = line.replace(space3,space0)
    if space2 in line:
        line = line.replace(space2,space1)
    line = line.replace(" ",",")
    line = line.replace("D","e")
    value_SI="0"
    try:
        component = line.split(",")[0]
        value_SI = line.split(",")[3]
    except IndexError:
        print(line)
    newline = component+","+value_SI
    newline = line
    return newline

dipole_input_section = lines[dipole_start_i[0]:dipole_start_i[0]+6+1]
dipole_dipole_section = lines[dipole_start_i[1]:dipole_start_i[1]+6+1]
alpha_input_section = lines[alpha_start_i[0]:alpha_start_i[0]+22]
alpha_dipole_section = lines[alpha_start_i[1]:alpha_start_i[1]+22]
beta_input_section = lines[beta_start_i[0]+3:beta_start_i[0]+74]
beta_dipole_section = lines[beta_start_i[1]+3:beta_start_i[1]+74]
gamma_input_section = lines[gamma_start_i[0]+3:gamma_start_i[0]+121]
gamma_dipole_section = lines[gamma_start_i[1]+3:gamma_start_i[1]+121]

# print(beta_input_section)

def convert_line(section,keyword="Alpha"):
    new_section = []
    for line in section:
        if (keyword in line) or ("SI" in line):
            pass
        else:
            newline = convert_char(line)
            new_section.append(newline)
    return new_section

dipole_input = convert_line(dipole_input_section,keyword="dipole")
dipole_dipole = convert_line(dipole_dipole_section,keyword="dipole")
alpha_input = convert_line(alpha_input_section,keyword="Alpha")
alpha_dipole = convert_line(alpha_dipole_section,keyword="Alpha")
beta_input = convert_line(beta_input_section,keyword="Beta")
beta_dipole = convert_line(beta_dipole_section,keyword="Beta")
gamma_input = convert_line(gamma_input_section,keyword="Gamma")
gamma_dipole = convert_line(gamma_dipole_section,keyword="Gamma")

# print(gamma_input)

def extract_dipole(value_list):
    component_list = ["Tot","x","y","z"]
    dipole = np.zeros(np.shape(component_list),dtype=float)
    for i,val in enumerate(value_list):
        component = val.split(",")[0]
        value_SI = float(val.split(",")[3].replace("\n",""))
        try:
            ind = component_list.index(component)
        except:
            print("cannot find the component ",component)
        dipole[ind] = value_SI
    return {"component":component_list,"dipole":dipole}
        

def extract_alpha(value_list):
    component_list = ["iso","aniso","xx","yx","yy","zx","zy","zz"]
    static = np.zeros(np.shape(component_list),dtype=float)
    ww_530 = np.zeros(np.shape(component_list),dtype=float)
    ww_1060 = np.zeros(np.shape(component_list),dtype=float)
    counter = 0
    for i,val in enumerate(value_list):
        component = val.split(",")[0]
        value_SI = float(val.split(",")[3].replace("\n",""))
        try:
            ind = component_list.index(component)
        except:
            print("cannot find the component ",component)
        if counter == 0:
            static[ind] = value_SI
        elif counter == 1:
            ww_1060[ind] = value_SI
        elif counter ==2:
            ww_530[ind] = value_SI
        if component == "zz":
            counter += 1
    return {"component":component_list,"static":static,
            "w=530":ww_530,"w=1060":ww_1060}

def extract_beta(value_list):
    component_list = ["parallel(z)","perpendicular(z)","x","y","z","parallel"]
    a = ["x","y","z"]
    for i in a:
        for j in a:
            for k in a:
                component_list.append(i+j+k)
    static = np.zeros(np.shape(component_list),dtype=float)
    ww_530 = np.zeros(np.shape(component_list),dtype=float)
    ww_1060 = np.zeros(np.shape(component_list),dtype=float)
    w2w_530 = np.zeros(np.shape(component_list),dtype=float)
    w2w_1060 = np.zeros(np.shape(component_list),dtype=float)
    counter = 0
    for i,val in enumerate(value_list):
        component = val.split(",")[0]
        value_SI = float(val.split(",")[3].replace("\n",""))
        try:
            ind = component_list.index(component)
        except:
            print("cannot find the component ",component)
        if counter == 0:
            static[ind] = value_SI
        elif counter == 1:
            ww_1060[ind] = value_SI
        elif counter ==2:
            ww_530[ind] = value_SI
        elif counter == 3:
            w2w_1060[ind] = value_SI
        elif counter == 4:
            w2w_530[ind] = value_SI
        if component == "zzz":
            counter += 1
    return {"component":component_list,"static":static,
            "w=530":ww_530,"w=1060":ww_1060,
            "2w=530":w2w_530,"2w=1060":w2w_1060}    

def extract_gamma(value_list):
    component_list = ["parallel","perpendicular"]
    a = ["x","y","z"]
    for i in a:
        for j in a:
            for k in a:
                for l in a:
                    component_list.append(i+j+k+l)
    static = np.zeros(np.shape(component_list),dtype=float)
    ww_530 = np.zeros(np.shape(component_list),dtype=float)
    ww_1060 = np.zeros(np.shape(component_list),dtype=float)
    w2w_530 = np.zeros(np.shape(component_list),dtype=float)
    w2w_1060 = np.zeros(np.shape(component_list),dtype=float)
    counter = 0
    for i,val in enumerate(value_list):
        component = val.split(",")[0]
        value_SI = float(val.split(",")[3].replace("\n",""))
        try:
            ind = component_list.index(component)
        except:
            print("cannot find the component ",component)
        if counter == 0:
            static[ind] = value_SI
        elif counter == 1:
            ww_1060[ind] = value_SI
        elif counter ==2:
            ww_530[ind] = value_SI
        elif counter == 3:
            w2w_1060[ind] = value_SI
        elif counter == 4:
            w2w_530[ind] = value_SI
        if component == "zzzz":
            counter += 1
    return {"component":component_list,"static":static,
            "w=530":ww_530,"w=1060":ww_1060,
            "2w=530":w2w_530,"2w=1060":w2w_1060}  

output_dir = "..\\polar-extract\\{}\\".format(filename)
pathlib.Path(output_dir).mkdir(exist_ok=True)
fname_output = output_dir
dipole_header = "component,dipole moment \n"
alpha_header = "component,Alpha(0;0),Alpha(-w;w) w=530nm,Alpha(-w;w) w=1060nm \n"
beta_header = "component,Beta(0;0,0),Beta(-w;w,0) w=1060nm,"+ \
    "Beta(-w;w,0) w=530.0nm,Beta(-2w;w,w) w=1060nm,Beta(-2w;w,w) w=530.0nm \n"
gamma_header = "component,Gamma(0;0,0),Gamma(-w;w,0) w=1060nm,"+ \
    "Gamma(-w;w,0) w=530.0nm,Gamma(-2w;w,w) w=1060nm,Gamma(-2w;w,w) w=530.0nm \n"

data = extract_dipole(dipole_input)
print("dipole input")
with open(fname_output+"dipole-input.csv","w") as f:
    f.writelines(dipole_header)
    for i,j in zip(data["component"],data["dipole"]):
        line = i+","+str(j)+"\n"
        f.writelines(line)

data = extract_dipole(dipole_dipole)
print("dipole dipole")
with open(fname_output+"dipole-dipole.csv","w") as f:
    f.writelines(dipole_header)
    for i,j in zip(data["component"],data["dipole"]):
        line = i+","+str(j)+"\n"
        f.writelines(line)
        
data = extract_alpha(alpha_input)
print("alpha input")
with open(fname_output+"alpha-input.csv","w") as f:
    f.writelines(alpha_header)
    for i,j,k,l in zip(data["component"],data["static"],data["w=530"],data["w=1060"]):
        line = i+","+str(j)+","+str(k)+","+str(l)+"\n"
        f.writelines(line)

data2 = extract_alpha(alpha_dipole)
print("alpha dipole")
with open(fname_output+"alpha-dipole.csv","w") as f:
    f.writelines(alpha_header)
    for i,j,k,l in zip(data2["component"],data2["static"],data2["w=530"],data2["w=1060"]):
        line = i+","+str(j)+","+str(k)+","+str(l)+"\n"
        f.writelines(line)

data3 = extract_beta(beta_input)
print("beta input")
with open(fname_output+"beta-input.csv","w") as f:
    f.writelines(beta_header)
    for i,j,k,l,m,n in zip(data3["component"],data3["static"],data3["w=530"],
                            data3["w=1060"],data3["2w=530"],data3["2w=1060"]):
        line = i+","+str(j)+","+str(k)+","+str(l)+","+str(m)+","+str(n)+"\n"
        f.writelines(line)

data4 = extract_beta(beta_dipole)
print("beta dipole")
with open(fname_output+"beta-dipole.csv","w") as f:
    f.writelines(beta_header)
    for i,j,k,l,m,n in zip(data4["component"],data4["static"],data4["w=530"],
                            data4["w=1060"],data4["2w=530"],data4["2w=1060"]):
        if (j==0) and (k==0) and (l==0) and (m==0) and (n==0):
            pass
        else:
            line = i+","+str(j)+","+str(k)+","+str(l)+","+str(m)+","+str(n)+"\n"
            f.writelines(line)

data5 = extract_gamma(gamma_input)
print("gamma input")
with open(fname_output+"gamma-input.csv","w") as f:
    f.writelines(gamma_header)
    for i,j,k,l,m,n in zip(data5["component"],data5["static"],data5["w=530"],
                            data5["w=1060"],data5["2w=530"],data5["2w=1060"]):
        if (j==0) and (k==0) and (l==0) and (m==0) and (n==0):
            pass
        else:
            line = i+","+str(j)+","+str(k)+","+str(l)+","+str(m)+","+str(n)+"\n"
            f.writelines(line)

data6 = extract_gamma(gamma_dipole)
print("gamma dipole")
with open(fname_output+"gamma-dipole.csv","w") as f:
    f.writelines(gamma_header)
    for i,j,k,l,m,n in zip(data6["component"],data6["static"],data6["w=530"],
                            data6["w=1060"],data6["2w=530"],data6["2w=1060"]):
        if (j==0) and (k==0) and (l==0) and (m==0) and (n==0):
            pass
        else:
            line = i+","+str(j)+","+str(k)+","+str(l)+","+str(m)+","+str(n)+"\n"
            f.writelines(line)