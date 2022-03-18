# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 01:06:11 2022

@author: hclts
"""

import numpy as np
import pathlib

class Polar:
    '''
    get electric dipole, dipole polarizability, first dipole hyperpolarizability
    
    second dipole hyperpolarizability (in SI unit) from gaussian09 Polar output.
    
    directory: default=onedrive+hpc\\gaussian09\\

    filename: exclude ".out" file extension
    
    get_data() generates csv files in a subdirectory in polar-extract
    '''
    def __init__(self,directory,filename):
        onedrive = "D:\\OneDrive - Newcastle University\\"
        g09_dir = onedrive+"hpc\\gaussian09\\"
        sub_dir = g09_dir+directory
        self.filename = filename
        self.fname = sub_dir+filename+".out"
    
    def _get_sections(self,lines):
        dipole_start = " Electric dipole moment"
        dipole_start_i = []
        alpha_start = " Dipole polarizability, Alpha"
        alpha_start_i = []
        beta_start = " First dipole hyperpolarizability, Beta"
        beta_start_i = []
        gamma_start = " Second dipole hyperpolarizability, Gamma "
        gamma_start_i = []

        for i,val in enumerate(lines):
            if dipole_start in val:
                dipole_start_i.append(i)
            if alpha_start in val:
                alpha_start_i.append(i)
            if beta_start in val:
                beta_start_i.append(i)
            if gamma_start in val:
                gamma_start_i.append(i)
                
        dipole_input_section = lines[dipole_start_i[0]:dipole_start_i[0]+7]
        try:
            dipole_dipole_section = lines[dipole_start_i[1]:dipole_start_i[1]+7]
        except IndexError:
            print("dipole is zero.")
            dipole_dipole_section = None
        alpha_input_section = lines[alpha_start_i[0]:alpha_start_i[0]+32]
        try:
            alpha_dipole_section = lines[alpha_start_i[1]:alpha_start_i[1]+32]
        except IndexError:
            print("dipole is zero.")
            alpha_dipole_section = None
        beta_input_section = lines[beta_start_i[0]+3:beta_start_i[0]+126]
        try:
            beta_dipole_section = lines[beta_start_i[1]+3:beta_start_i[1]+126]
        except IndexError:
            print("dipole is zero.")
            beta_dipole_section = None
        gamma_input_section = lines[gamma_start_i[0]+3:gamma_start_i[0]+219]
        try:
            gamma_dipole_section = lines[gamma_start_i[1]+3:gamma_start_i[1]+219]
        except IndexError:
            print("dipole is zero.")
            gamma_dipole_section = None
        
        return (dipole_input_section,dipole_dipole_section,
                alpha_input_section,alpha_dipole_section,
                beta_input_section,beta_dipole_section,
                gamma_input_section,gamma_dipole_section)

    def _convert_char(self,line):
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

    def _convert_section(self,section,keyword="Alpha"):
        if section != None:
            new_section = []
            for line in section:
                if (keyword in line) or ("SI" in line):
                    pass
                else:
                    newline = self._convert_char(line)
                    new_section.append(newline)
        else:
            new_section = None
        return new_section

    def _get_dipole(self,value_list):
        component_list = ["Tot","x","y","z"]
        dipole = np.full_like(component_list,np.nan,dtype=float)
        if value_list != None:
            for i,val in enumerate(value_list):
                component = val.split(",")[0]
                value_SI = float(val.split(",")[3].replace("\n",""))
                try:
                    ind = component_list.index(component)
                except:
                    print("cannot find the component ",component)
                dipole[ind] = value_SI
        return {"component":component_list,"dipole":dipole}
            
    
    def _get_alpha(self,value_list):
        component_list = ["iso","aniso","xx","yx","yy","zx","zy","zz"]
        static = np.full_like(component_list,np.nan,dtype=float)
        ww_530 = np.full_like(component_list,np.nan,dtype=float)
        ww_1060 = np.full_like(component_list,np.nan,dtype=float)
        counter = 0
        if value_list != None:
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
    
    def _get_beta(self,value_list):
        component_list = ["parallel(z)","perpendicular(z)","x","y","z","parallel"]
        a = ["x","y","z"]
        for i in a:
            for j in a:
                for k in a:
                    component_list.append(i+j+k)
        static = np.full_like(component_list,np.nan,dtype=float)
        ww_530 = np.full_like(component_list,np.nan,dtype=float)
        ww_1060 = np.full_like(component_list,np.nan,dtype=float)
        w2w_530 = np.full_like(component_list,np.nan,dtype=float)
        w2w_1060 = np.full_like(component_list,np.nan,dtype=float)
        counter = 0
        if value_list != None:
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
    
    def _get_gamma(self,value_list):
        component_list = ["parallel","perpendicular"]
        a = ["x","y","z"]
        for i in a:
            for j in a:
                for k in a:
                    for l in a:
                        component_list.append(i+j+k+l)
        static = np.full_like(component_list,np.nan,dtype=float)
        ww_530 = np.full_like(component_list,np.nan,dtype=float)
        ww_1060 = np.full_like(component_list,np.nan,dtype=float)
        w2w_530 = np.full_like(component_list,np.nan,dtype=float)
        w2w_1060 = np.full_like(component_list,np.nan,dtype=float)
        counter = 0
        if value_list != None:
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

    def _export_csv(self,data,key1="dipole",key2="input"):
        csv_dir = "..\\polar-extract\\{}\\".format(self.filename)
        pathlib.Path(csv_dir).mkdir(exist_ok=True)
        dipole_header = "component,dipole moment\n"
        alpha_header = "component,Alpha(0;0),Alpha(-w;w) w=530nm,"+ \
            "Alpha(-w;w) w=1060nm\n"
        beta_header = "component,Beta(0;00),Beta(-w;w0) w=530nm,"+ \
            "Beta(-w;w0) w=1060nm,Beta(-2w;ww) w=530nm,Beta(-2w;ww) w=1060nm\n"
        gamma_header = "component,Gamma(0;00),Gamma(-w;w0) w=530nm,"+ \
            "Gamma(-w;w0) w=1060nm,Gamma(-2w;ww) w=530nm,Gamma(-2w;ww) w=1060nm\n"
        if (key1=="dipole") and (key2=="input"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(dipole_header)
                for i,j in zip(data["component"],data["dipole"]):
                    line = "{},{}\n".format(i,j)
                    f.writelines(line)
        elif (key1=="dipole") and (key2=="dipole"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(dipole_header)
                for i,j in zip(data["component"],data["dipole"]):
                    line = "{},{}\n".format(i,j)
                    f.writelines(line)
        elif (key1=="alpha") and (key2=="input"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(alpha_header)
                for i,j,k,l in zip(data["component"],data["static"],
                                   data["w=530"],data["w=1060"]):
                    if np.isnan(j) and np.isnan(k) and np.isnan(l):
                        pass
                    else:
                        line = "{},{},{},{}\n".format(i,j,k,l)
                        f.writelines(line)
        elif (key1=="alpha") and (key2=="dipole"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(alpha_header)
                for i,j,k,l in zip(data["component"],data["static"],
                                   data["w=530"],data["w=1060"]):
                    if np.isnan(j) and np.isnan(k) and np.isnan(l):
                        pass
                    else:
                        line = "{},{},{},{}\n".format(i,j,k,l)
                        f.writelines(line)
        elif (key1=="beta") and (key2=="input"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(beta_header)
                for i,j,k,l,m,n in zip(data["component"],data["static"],
                                       data["w=530"],data["w=1060"],
                                       data["2w=530"],data["2w=1060"]):
                    if (np.isnan(j) and np.isnan(k) and np.isnan(l) and 
                        np.isnan(m) and np.isnan(n)):
                        pass
                    else:
                        line = "{},{},{},{},{},{}\n".format(i,j,k,l,m,n)
                        f.writelines(line)
        elif (key1=="beta") and (key2=="dipole"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(beta_header)
                for i,j,k,l,m,n in zip(data["component"],data["static"],
                                       data["w=530"],data["w=1060"],
                                       data["2w=530"],data["2w=1060"]):
                    if (np.isnan(j) and np.isnan(k) and np.isnan(l) and 
                        np.isnan(m) and np.isnan(n)):
                        pass
                    else:
                        line = "{},{},{},{},{},{}\n".format(i,j,k,l,m,n)
                        f.writelines(line)
        elif (key1=="gamma") and (key2=="input"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(gamma_header)
                for i,j,k,l,m,n in zip(data["component"],data["static"],
                                       data["w=530"],data["w=1060"],
                                       data["2w=530"],data["2w=1060"]):
                    if (np.isnan(j) and np.isnan(k) and np.isnan(l) and 
                        np.isnan(m) and np.isnan(n)):
                        pass
                    else:
                        line = "{},{},{},{},{},{}\n".format(i,j,k,l,m,n)
                        f.writelines(line)
        elif (key1=="gamma") and (key2=="dipole"):
            print("{}-{}".format(key1,key2))
            fname_csv = csv_dir+"{}-{}.csv".format(key1,key2)
            with open(fname_csv,"w") as f:
                f.writelines(gamma_header)
                for i,j,k,l,m,n in zip(data["component"],data["static"],
                                       data["w=530"],data["w=1060"],
                                       data["2w=530"],data["2w=1060"]):
                    if (np.isnan(j) and np.isnan(k) and np.isnan(l) and 
                        np.isnan(m) and np.isnan(n)):
                        pass
                    else:
                        line = "{},{},{},{},{},{}\n".format(i,j,k,l,m,n)
                        f.writelines(line)
        
    def get_data(self):
        '''
        export data in csv files.
        '''
        f = open(self.fname,"r")
        lines = f.readlines()
        f.close()
        
        sections = self._get_sections(lines)
        dipole_input = self._convert_section(sections[0],keyword="dipole")
        dipole_dipole = self._convert_section(sections[1],keyword="dipole")
        alpha_input = self._convert_section(sections[2],keyword="Alpha")
        alpha_dipole = self._convert_section(sections[3],keyword="Alpha")
        beta_input = self._convert_section(sections[4],keyword="Beta")
        beta_dipole = self._convert_section(sections[5],keyword="Beta")
        gamma_input = self._convert_section(sections[6],keyword="Gamma")
        gamma_dipole = self._convert_section(sections[7],keyword="Gamma")
        
        dipole_input_data = self._get_dipole(dipole_input)
        dipole_dipole_data = self._get_dipole(dipole_dipole)
        alpha_input_data = self._get_alpha(alpha_input)
        alpha_dipole_data = self._get_alpha(alpha_dipole)
        beta_input_data = self._get_beta(beta_input)
        beta_dipole_data = self._get_beta(beta_dipole)
        gamma_input_data = self._get_gamma(gamma_input)
        gamma_dipole_data = self._get_gamma(gamma_dipole)
        
        self._export_csv(dipole_input_data,key1="dipole",key2="input")
        self._export_csv(dipole_dipole_data,key1="dipole",key2="dipole")
        self._export_csv(alpha_input_data,key1="alpha",key2="input")
        self._export_csv(alpha_dipole_data,key1="alpha",key2="dipole")
        self._export_csv(beta_input_data,key1="beta",key2="input")
        self._export_csv(beta_dipole_data,key1="beta",key2="dipole")
        self._export_csv(gamma_input_data,key1="gamma",key2="input")
        self._export_csv(gamma_dipole_data,key1="gamma",key2="dipole")
        
        print("Done.")
        
        
        


        