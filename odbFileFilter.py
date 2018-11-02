#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 21:36:08 2018

@author: matterholt
"""

import re
import os, sys

#--to check --
testlist = [
        'analysis_T3C_FrSub_V30r00-FtPOS.odb',
        'Analysis_tsx_FrSub_v34r02_FhPOS.odb',
        'analysis_4GS_FrSub_V62r20-MBNeg.odb',
        'Analysis_I0S_FrSub_V11r625-MTpos.odb',
        'Analysis_I0S_FrSub_V11r625-MTpos.inp',
        'Analysis_I0S_FrSub_V11r625-MTpos.msg',
        'Analysis_I0S_FrSub_V11r625-MTpos.dat',
        'Analysis_I0S_FrSub_V11r625-ftpos.odb_f',
        'Analysis_2SU_FrSub_V00r00-mbneg.odb',
        'Analysis_PKND_FrSub_V52r83_fhpos.odb',
        'Analysis_5NIV_FrSub_V30r05a_MBNEG.odb']


#Define that working file
#path = "openOdb('analysis_camGuide_v09r00-v35r09b.odb')"
#dirs = os.listdir(path)

fileList = []
cleanList = []
errorList = []

#
def GetFiles(dirs):
    for file in dirs:
        fileList.append(file)
    
#remove files the do not meet the the regex of .odb
def CleanFiles(fileList):
    for file in fileList:
        pattern = r"(\w+\S+.odb)"
        match = re.fullmatch(pattern, file)
        if match:
            cleanList.append(file)
        else:
            errorList.append(file)

CleanFiles(testlist)
print('\nFiles did not meet requirement')
print(errorList)
print('\nFiles that will be processed')
print(cleanList)

#for the list of corect files 

'''


'''

#pattern = r"([vV]\d+[rR].*(?=.odb))"
