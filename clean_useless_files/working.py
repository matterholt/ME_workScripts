"""
Script to obtain info on the file within a given directory. Data will be exported as a csv file
"""

import os
from save_doc import save_report_json

from time import  strftime, gmtime
#from doc_graph import scatt_graph


class File_Data:
    def __init__ (self,subdir,dirs,file_name):
        self.subdir = subdir
        self.dirs = dirs
        self.file_name = file_name
        self.file_path  = self.subdir + os.sep + self.file_name

    def file_type_extension(self):
       return os.path.splitext(self.file_path)[1]

    def year_file_accessed(self):
        access_date_file = os.stat(self.file_path).st_mtime
        file_access_year = strftime("%Y", gmtime(access_date_file))
        return file_access_year

    def file_size_KB(self):
        return os.stat(self.file_path).st_size
    
    def __str__(self):
        return self.file_name
      

def take_inventory_dir(dir_path, file_requirements):
    """
    cycle through a directory searching for files,

    """

    file_path_error = 0

    other_file_list = []
    junk_file_list = []
    review_file_list = []

    for subdir, dirs, files in os.walk(dir_path):
        for file_name in files:
            try:
                file_specs = File_Data(subdir, dirs, file_name)
                file_type_extension = file_specs.file_type_extension()
                
                if file_type_extension in file_requirements["review_file"]:
                    review_file_list.append(file_specs)

                if file_type_extension in file_requirements["junk_file"]:
                    junk_file_list.append(file_specs)
                    
                else:
                    other_file_list.append(file_specs)

            except FileNotFoundError:
                file_path_error += 1
                
    file_bundle = {
            "file_error" :file_path_error,
            "review_files" : review_file_list,
            "junk_files" : junk_file_list,
            "other_files": other_file_list
            }
    return file_bundle

def parse_file_info(file):
    if "file_error" in file:
        del file["file_error"]
    
    doc_try = []
#    temp_json = json.dumps(file)
    for file_category in file.keys():
        data_stage = file[file_category]
        data_list = {'file_category':file_category,'file_data':[]}
        for x in data_stage:
            data = {
                        "name": x.file_name,
                        "year": x.year_file_accessed(),
                        "size": x.file_size_KB(),
                        "extension": x.file_type_extension()
                        }
            data_list['file_data'].append(data)
        doc_try.append(data_list)

    return doc_try    
            
def main(working_dir, file_requirements):
#    current_work_dir = os.getcwd()

    dir_evaluation = take_inventory_dir(working_dir, file_requirements)
    working_data = parse_file_info(dir_evaluation)
    save_report_json(working_data)
    


    
if __name__ == "__main__":
        #    working_dir = r"F:"
    working_dir = r"S:\V2\mesh"

    
    file_requirements = {
            "junk_file" : [".html", ".out", ".res", ".stat",".sta",".f04",
                              ".mesg", ".mvw"],
            "review_file": ['.hm', '.inp', '.fem','.CATAnalysis','CATPart',
                            '.avi','lms']
            }

    main(working_dir,file_requirements)
    
    
    
    #############################################
    
    # -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 10:01:25 2020

@author: MATTERHOLT
"""
import csv
import json


def save_report_csv(dict_stat,current_work_dir):

    saved_dir_file_name = f"{current_work_dir}\\checks_TESTING.csv"
    
    with open(saved_dir_file_name,'w', newline='') as csv_file:
        data_writer = csv.writer(csv_file, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for file_data in dict_stat:
            year = str(file_data.year_file_accessed())
            size = str(file_data.file_size_KB())
            path = file_data.file_path
    
            data_writer.writerow([year,size,path])
    
    print(saved_dir_file_name)
    
def save_report_json(working_list,):
    # Serializing json  
    json_object = json.dumps(working_list, indent = 2) 
      
    # Writing to sample.json 
    with open("sample.json", "w") as outfile: 
        outfile.write(json_object)
    
    print("file saved")
    
    
    #############################
    # -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 09:02:18 2020

@author: MATTERHOLT
question for analysis report

1. what files are being stored
    - what type? , what year?, space taken up on hard drive
"""
from bokeh.plotting import figure, output_file, show
import json

def year_summary(year_list):
    list_summary = {}
    
    for year in year_list:
        list_summary[year] = list_summary.get(year,0)+1
    
    return list_summary

def year_count(data_struct):
    """
    reduce object to a list of years
    """
    year =[]
    for key in data_struct['file_data']:
        year.append(key['year'])
        
    summary = year_summary(year)
    return summary        



def bar_graph(inputs):
    output_file("year_count.html")
    
    years = list(inputs.keys())
    year_freq = list(inputs.values())
    
    #sort by data
    year_sort = sorted(years)

    p = figure(plot_width=400, plot_height=400, x_range=year_sort)
    
    p.vbar(x=years, top=year_freq,width=0.5,color="navy", alpha=0.5)
    
    show(p)
    

def main(file_inventory):

    
    section_one = file_inventory[0]
    
    section_year_count = year_count(section_one)

    bar_graph(section_year_count)
    
if __name__ == "__main__":
    file_data  = None
    
    data_file = r"sample.json"
    with open(data_file)as f:
        file_data = json.load(f)
        
    main(file_data)
