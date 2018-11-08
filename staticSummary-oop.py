#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:56:06 2018

@author: matterholt
"""
#, dof, nodeNumb, system
#,'3', '111', 'LOCAL'

class StaticSummary:
    def __inif__ (self, fileName, loadCase):
        self.fileName = fileName
        self.loadCase = loadCase
#        self.odbFile = fileName[0:-4]+".odb"
#        self.dof = dof
#        self.nodeNumb = nodeNumb
#        self.system = system
        
file = StaticSummary('analysis_example-Ftpos.inp', 'MBpos')
