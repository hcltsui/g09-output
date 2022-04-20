# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 01:35:14 2022

@author: hclts
"""

from g09_output import Polar

##############################################################################
# lead perovskite

def lead_perovskite():
    MAPbCl3_1 = Polar("MAPbCl3\\no_symm-full\\","MAPbCl3-no_symm-full-b3lyp-lanl2dz")
    #MAPbCl3_1.get_data()
    
    MAPbI3_1 = Polar("MAPbI3\\no_symm-full\\","MAPbI3-no_symm-full-b3lyp-lanl2dz")
    #MAPbI3_1.get_data()

##############################################################################

def MAPbBr3():
    MAPbBr3 = Polar("MAPbBr3\\no_symm-full\\","MAPbBr3-no_symm-full-b3lyp-lanl2dz")
    #MAPbBr3.get_data()
    
    MAPbBr3_1 = Polar("MAPbBr3\\polar-1\\","MAPbBr3-polar-1-b3lyp-lanl2dz")
    MAPbBr3_2 = Polar("MAPbBr3\\polar-2\\","MAPbBr3-polar-2-b3lyp-lanl2dz")
    MAPbBr3_3 = Polar("MAPbBr3\\polar-3\\","MAPbBr3-polar-3-b3lyp-gen")
    
    for i in [MAPbBr3_1,MAPbBr3_2,MAPbBr3_3]:
        i.get_data()
##############################################################################
# lead based octahedral

def lead_octahedral():
    PbBr6_1 = Polar("MAPbBr3-PbBr6\\1545320\\","MAPbBr3-1545320-PbBr6-b3lyp-lanl2dz")
    PbBr6_1.get_data()
    
    PbBr6_2 = Polar("MAPbBr3-PbBr6\\4516751\\","MAPbBr3-4516751-PbBr6-b3lyp-lanl2dz")
    PbBr6_2.get_data()
    
    PbBr6_3 = Polar("MAPbBr3-PbBr6\\wmd\\","MAPbBr3-wmd-PbBr6-b3lyp-lanl2dz")
    PbBr6_3.get_data()
    
    PbCl6_1 = Polar("MAPbCl3-PbCl6\\7231905\\","MAPbCl3-7231905-PbCl6-b3lyp-lanl2dz")
    PbCl6_1.get_data()
    
    PbCl6_2 = Polar("MAPbCl3-PbCl6\\wmd\\","MAPbCl3-wmd-PbCl6-b3lyp-lanl2dz")
    PbCl6_2.get_data()
    
    PbI6_1 = Polar("MAPbI3-PbI6\\7225287\\","MAPbI3-7225287-PbI6-b3lyp-lanl2dz")
    PbI6_1.get_data()
    
    PbI6_2 = Polar("MAPbI3-PbI6\\7236651\\","MAPbI3-7236651-PbI6-b3lyp-lanl2dz")
    PbI6_2.get_data()
    
    PbI6_3 = Polar("MAPbI3-PbI6\\wmd\\","MAPbI3-wmd-PbI6-b3lyp-lanl2dz")
    PbI6_3.get_data()

##############################################################################
# metal-free perovskite

def metal_free_perovskite():
    MDNI_1 = Polar("MDNI\\no_symm-full\\","MDNI-no_symm-full-b3lyp-321g")
    MDNI_1.get_data()
    
    MDNI_2 = Polar("MDNI\\no_symm-full-no_charge\\","MDNI-no_symm-full-no_charge-b3lyp-321g")
    MDNI_2.get_data()
    
    MDNBr_1 = Polar("MDNBr\\no_symm-full\\","MDNBr-no_symm-full-b3lyp-321g")
    MDNBr_1.get_data()
    
    MDNBr_2 = Polar("MDNBr\\no_symm-full-no_charge\\","MDNBr-no_symm-full-no_charge-b3lyp-321g")
    MDNBr_2.get_data()

##############################################################################
# metal-free

def metal_free_octahedral():
    NH4Br6 = Polar("MDNBr-NH4Br6\\b3lyp\\3-21g-1\\","MDNBr-NH4Br6-b3lyp-321g")
    NH4Br6.get_data()
    
    NH4I6 = Polar("MDNI-NH4I6\\b3lyp\\3-21g-1\\","MDNI-NH4I6-b3lyp-321g")
    NH4I6.get_data()
    
    DABCO = Polar("DABCO\\b3lyp\\3-21g-1\\","DABCO-b3lyp-321g")
    DABCO.get_data()
    
    MDABCO = Polar("MDABCO\\b3lyp\\3-21g-1\\","MDABCO-b3lyp-321g")
    MDABCO.get_data()
    
    MDNI_MDABCO = Polar("MDNI-MDABCO\\MDNI-R3-MDABCO\\","MDNI-MDABCO-b3lyp-321g")
    MDNI_MDABCO.get_data()
    
    MDNBr_MDABCO = Polar("MDNBr-MDABCO\\MDNBr-R3-MDABCO\\","MDNBr-MDABCO-b3lyp-321g")
    MDNBr_MDABCO.get_data()

##############################################################################
# methylammonium

def methylammonium():
    MA_Br = Polar("MAPbBr3-MA\\no_symm-full\\","MAPbBr3-MA-no_symm-full-b3lyp-lanl2dz")
    MA_Br.get_data()

    MA_Cl = Polar("MAPbCl3-MA\\no_symm-full\\","MAPbCl3-MA-no_symm-full-b3lyp-lanl2dz")
    MA_Cl.get_data()

    MA_I = Polar("MAPbI3-MA\\no_symm-full\\","MAPbI3-MA-no_symm-full-b3lyp-lanl2dz")
    MA_I.get_data()
    
    MA = Polar("MA\\standalone\\","MA-standalone-b3lyp-lanl2dz")
    MA.get_data()

##############################################################################
# methylammonium parts

def MA_Br_parts():
    MA_Br_1 = Polar("MAPbBr3-MA\\1\\","MAPbBr3-MA-1-b3lyp-lanl2dz")
    MA_Br_1.get_data()

    MA_Br_2_inline = Polar("MAPbBr3-MA\\2-inline\\","MAPbBr3-MA-2-inline-b3lyp-lanl2dz")
    MA_Br_2_inline.get_data()

    MA_Br_2_parallel = Polar("MAPbBr3-MA\\2-parallel\\","MAPbBr3-MA-2-parallel-b3lyp-lanl2dz")
    MA_Br_2_parallel.get_data()

    MA_Br_4_inplane = Polar("MAPbBr3-MA\\4-inplane\\","MAPbBr3-MA-4-inplane-b3lyp-lanl2dz")
    MA_Br_4_inplane.get_data()

    MA_Br_4_outplane = Polar("MAPbBr3-MA\\4-outplane\\","MAPbBr3-MA-4-outplane-b3lyp-lanl2dz")
    MA_Br_4_outplane.get_data()

##############################################################################
# methylammonium parts with Br and Pb

def MA_Br_variations():
    work_dir = "MAPbBr3-MA\\variations\\"
    MA_1_Br = Polar(work_dir,"MAPbBr3-MA-1-Br-b3lyp-lanl2dz")
    MA_1_Pb = Polar(work_dir,"MAPbBr3-MA-1-Pb-b3lyp-lanl2dz")
    MA_2_inline_Br = Polar(work_dir,"MAPbBr3-MA-2-inline-Br-b3lyp-lanl2dz")
    MA_2_inline_Pb = Polar(work_dir,"MAPbBr3-MA-2-inline-Pb-b3lyp-lanl2dz")
    MA_2_parallel_Br = Polar(work_dir,"MAPbBr3-MA-2-parallel-Br-b3lyp-lanl2dz")
    MA_2_parallel_Pb = Polar(work_dir,"MAPbBr3-MA-2-parallel-Pb-b3lyp-lanl2dz")
    MA_4_inplane_Br = Polar(work_dir,"MAPbBr3-MA-4-inplane-Br-b3lyp-lanl2dz")
    MA_4_inplane_Pb = Polar(work_dir,"MAPbBr3-MA-4-inplane-Pb-b3lyp-lanl2dz")
    MA_4_outplane_Br = Polar(work_dir,"MAPbBr3-MA-4-outplane-Br-b3lyp-lanl2dz")
    MA_4_outplane_Pb = Polar(work_dir,"MAPbBr3-MA-4-outplane-Pb-b3lyp-lanl2dz")
    MA_8_Br = Polar(work_dir,"MAPbBr3-MA-8-Br-6-b3lyp-lanl2dz")
    MA_8_Pb = Polar(work_dir,"MAPbBr3-MA-8-Pb-b3lyp-lanl2dz")
    for MA in [MA_1_Br,MA_1_Pb,MA_2_inline_Br,MA_2_inline_Pb,MA_2_parallel_Br,
               MA_2_parallel_Pb,MA_4_inplane_Br,MA_4_inplane_Pb,MA_4_outplane_Br,
               MA_4_outplane_Pb,MA_8_Br,MA_8_Pb]:
        MA.get_data()

def MA_Br_variations_2():
    work_dir = "MAPbBr3-MA\\variations-2\\"
    MA_1 = Polar(work_dir,"MAPbBr3-MA-1-Br-Pb-b3lyp-lanl2dz")
    MA_2_inline = Polar(work_dir,"MAPbBr3-MA-2-inline-Br-Pb-b3lyp-lanl2dz")
    MA_2_parallel = Polar(work_dir,"MAPbBr3-MA-2-parallel-Br-Pb-b3lyp-lanl2dz")
    MA_4_inplane = Polar(work_dir,"MAPbBr3-MA-4-inplane-Br-Pb-b3lyp-lanl2dz")
    MA_4_outplane = Polar(work_dir,"MAPbBr3-MA-4-outplane-Br-Pb-b3lyp-lanl2dz")
    MA_8 = Polar(work_dir,"MAPbBr3-MA-8-Br-6-Pb-b3lyp-lanl2dz")
    for MA in [MA_1,MA_2_inline,MA_2_parallel,
               MA_4_inplane,MA_4_outplane,MA_8]:
        MA.get_data()
##############################################################################
# Br variations

def Br_variations():
    work_dir = "MAPbBr3-Br\\variations-1\\"
    Br_2 = Polar(work_dir,"MAPbBr3-Br-2-b3lyp-lanl2dz")
    Br_4 = Polar(work_dir,"MAPbBr3-Br-4-b3lyp-lanl2dz")
    Br_6 = Polar(work_dir,"MAPbBr3-Br-6-b3lyp-lanl2dz")
    for Br in [Br_2,Br_4,Br_6]:
        Br.get_data()
###############################################################################

if __name__ == "__main__":
    MAPbBr3()