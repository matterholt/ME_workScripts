"""
main file,

process
1. location odb within a directory , odb must have associated .inp file
2. use inp to extract load parameters.
3. extract force/displacement curve data from the odb file
4. use Bokeh lib to create curve
5. save data to csv file
6. move odb into results folder


feature:
    make a log file of file that are check, one not check and any errors
"""
import os
import re


def main():
    path = os.getcwd()
    directory_file_in_cwd = os.listdir(path)

    class Result_file:
        def __init__(self, odb_file, inp_file,):
            self.odb_file = odb_file
            self.inp_file = inp_file

        def get_model_VerRev(self):
            pattern_VerRev = re.compile(r"[a|A]nalysis_\S+[-|_](\w+).odb")
            model_name = pattern_VerRev.match(self.odb_file)
            return model_name

    class Load_data():
        def __init__(self, system_type, node_load, direction_load):
            self.system_type = system_type
            self.node_load = node_load
            self.direction_load = direction_load

        def get_displacement(self):
            """
            working progress, hard to test since need an ODB
            this will build the string that will lead to the path in the ODB
            code need to support python2.8
            """
            last_step = steps['Step-1']
            hist_reg = last_step.historyRegions['Node PART-1-1.' + self.node_load]
            hist_out = hist_reg.historyOutputs['U' +
                                               self.direction_load + ' ' + self.system_type]
            disp_force_data = hist_out.data
            return disp_force_data


if __name__ == '__main__':
    main()
