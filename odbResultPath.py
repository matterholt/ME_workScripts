#-*- coding: utf-8 -*-
"""

need to be Python 2 due to Abaqus scripting
!!! need to set up some regex to make sure no other 
!!! value is entered!!
"""

#===========================================
#Defines the load step for displacement / ReactionForce
#===========================================
def LoadStep():
    defaultStep = input('Default "Step-1" OK% \nhit Enter to confirm or "n" To change Step number: ')
    if defaultStep == "n":
        newStepNum = input("Enter Step number: ")
        loadStepResult = "Step-"+newStepNum
        print("--> Step is applied in " + loadStepResult)
        return loadStepResult
 
    elif defaultStep == "" or defaultStep =='y':
        loadStep = "Step-1"
        print("--> Step is applied in " + loadStep)
        return loadStep

    else:
        print("!!! --> "+ defaultStep + "is invalid")
        return LoadStep()
#===========================================
#Defines the Analysis System for which direction of load 
#===========================================
def DefineSystem():
    systemDef = input('DEFAULT "LOCAL" system OK? \nEnterofr Local or g for global:  ' ).lower()
    print(systemDef)
    if systemDef == 'l' or systemDef == "":
        print('--> Load is applied in "LOCAL" ')
        return "LOCAL"
    elif systemDef == 'g':
        print('--> Load is applied in "GOBAL" ')
        return "GLOBAL"
    else:
        print("!!!" + systemDef + "invalid value")
        return DefineSystem()
#===========================================
#Defines the Node number for which the load is applied
#!!! need to make sure in does not go to the next step until 
#===========================================
def DefineNodeNum():
    node = input("Load applied Node number: ")
    output = "Node PART-1-1." + node
    print ("--> Load applied to " + node)
    return output
#===========================================
#Defines the Node number for which the load is applied
#===========================================
def LoadDirections ():
    directions = {
    "x" : "1",
    "y" : "2",
    "z" : "3",
    "xx" : "4",
    "yy" : "5",
    "zz" : "6"
    }
    loadDir = input("Load Direction is applied: ").lower()
    if loadDir in directions.keys():
        print("--> Load applied in " + loadDir)
        return directions[loadDir]
    elif loadDir in directions.values():
        print("--> Load applied in " + loadDir)
        return loadDir
    else:
        print("!!!" + "invalid value!")
        return LoadDirections ()




step = LoadStep()
system = DefineSystem()
node = DefineNodeNum()
direction = LoadDirections ()
rfDir = "RF"+ direction + " " + system
uDir = "U"+ direction + " " + system


print("\n\n================SUMMARY================")
print("--> curve wil be checked on " + '(' + step +')')
print("--> Load is applied in " + '(' + system +')')
print("--> Load is on node" + '(' +  node +')')
print("--> Load being applied in the " + '(' +  direction +')')
print("--> Reaction Force value: " + '(' + rfDir +')')
print("--> Dispacement value: "+ '(' + uDir +')')

print("\n\n================RESULT================")
#remove quotes to get to work with abaqus scritpt,,
reactionForce = '(odb.steps['+step+'].historyRegions['+node+'].historyOutputs['+rfDir+'].data'
displacement = '(odb.steps['+step+'].historyRegions['+node+'].historyOutputs['+uDir+'].data'

print(reactionForce)
print(displacement)