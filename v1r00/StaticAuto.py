#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:56:06 2018

@author: matterholt
"""

import os 
import re
#from odbAccess import *
def main():
    
    
    odbFilesList = os.listdir(testDir)
    path = os.getcwd()

#    resultLocation = input(Static file locaton:)
    
####Test 
    testDir = "//"
    resultLocation = testDir
    
    #Dictionary for for each analysis --> is this the best way??
    staticInfo = {
    #        "loadCase"  : "mbpos",
    #        "inpName"   : "*.inp",
    #        "odbName"   : "*.odb",
    #        "loadDir"   : "2",
    #        "nodeNumb"  : "432",
    #        "system"    : "LOCAL"
            }
    noRunList = []
    
    
    
# =============================================================================
#     Filter file and find Values fo staticInfo Dictonary: 
#       Results : (odbFile, LoadCase, InpName)
# =============================================================================
    def filterFiles(file):
        patternOdb = r"([a|A]nalysis_\S+[-|_](\w+).odb)"
        odbMatch = re.match(patternOdb, file)
        if odbMatch:
            staticInfo["odbName"] = file
            staticInfo["loadCase"] = odbMatch.group(2)
            staticInfo["inpName"] = file[0:-4] + '.inp'
        else:
            noRunList.append(file)
    
# =============================================================================
# Read line to find Load Direction and Node Number
# =============================================================================
    def nodeLoad(line):
        stringPattern = r"\*MONITOR,DOF=(\d+),NODE=(\d+)"
        loadMatch=  re.match(stringPattern. line)
        if loadMatch:
            staticInfo["loadDir"] = loadMatch.group(1)
            staticInfo["nodeNumb"] = loadMatch.group(2)
    
# =============================================================================
# Read line to find if Load is applied in Local or Global 
# =============================================================================
    def systemLoad(line):
        systemPattern = r"global= NO"
        staticInfo["system"] = "GLOBAL"
        systemMatch = re.search(systemPattern,line)
        if systemMatch:
            staticInfo["system"] = "LOCAL"
        
# =============================================================================
# Looks in directory for files
# =============================================================================
    def findfile():
        for file in odbFilesList:
            filterFiles(file)

# =============================================================================
# Reads inp file line by line
# =============================================================================
    def readFileLine():
        inpFile = resultLocation + staticInfo["inpName"]
        fileLine = open(inpFile,"r")
        for line in fileLine:
            nodeLoad(line)
            systemLoad(line)
        fileLine.close()
        

# =============================================================================
# Fire code
# =============================================================================
    findfile()
    readFileLine()
    
# =============================================================================
#   Prints and info to call to view
# =============================================================================
    def printDict ():
        print("Dictonary's Contents")
        print(staticInfo)
    def printStaticSummary ():
        print("\n\n" + "-"*10 + "STATIC FILE REVIEW"+ "-"*10 )
        print("Analysis file is ------------> " + staticInfo['inpName'])
        print("Load Case is ----------------> " + staticInfo['loadCase'])
        print("load applied ----------------> " + staticInfo['loadDir'])
        print("Node Number -----------------> " + staticInfo['nodeNumb'])
        print("System for analysis ---------> " + staticInfo['system'])
        print("Results file ----------------> " + staticInfo['odbName'])
    def failedFile ():
        print("\n\n" + "-"*10 + "Files did not meet Requirements"+ "-"*10)
        for fileFail in noRunList:
            print("FAILED ----> " + fileFail)
# =============================================================================
# Define odb results path
# =============================================================================
    def dataFind ():
        odbFileName = staticInfo['odbName']
        node = staticInfo['loadDir'}
        odb = openOdb(odbFileName)
        #!!CHECK IT IF PATH IS CORRECT!!!
        restulsPath = (odb.steps['Step-1'].historyRegions['NODE PART-1.1.'+])
    
if __name__ == "__main__":
    main()
    
    