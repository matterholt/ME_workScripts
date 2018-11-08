The code is ment to take two list extract strip the second value in the in both lists
and combine them to create a curve.
I use the the script to combine the Displacemnet and the Reaction Force.

The u is displacement and the rf is the reaction force.

The purpose for this script is that instead of opening the program and saving the file I hope to be
able to exicute the script and have the bulk of the work done.

This is just a step for what I want to do .

## Process

1. script will go to a user defined directory
2. filter out the files that don't meet requirement -> example: "analysis_loadcase.inp"
3. for the filename will extract 3 values<br>
   3.1 file name <br>
   3.2 load case<br>
   3.3 create .odb file name from .inp file
4. Search for direction of node<br>
   4.1 regex search for accuator<br>
   -- r"*NSET,NSET=ACTUATOR\N(\d+)"<br>
   4.2 regex search for *MONITOR <br>
   -- r"\*MONITOR,DOF=(\d+),NODE=(\d+)" group1
5. Search for direction of load<br>
   5.1 regex search for actuator
   -- r"ACTUATOR,(\d),\d,\d.0"
   5.2 regex search for *MONITOR <br>
   -- r"*MONITOR,DOF=(\d+),NODE=(\d+)" group2

### retrun should be:

[filename, loadCase, odbname, nodenumb, dof, system']
