"""
In the supplied directory script searches all the files and obtain type of file, path to the file, size of file and the year that it was last accessed. Once the script has search directory will save a json file in the current workind directory  
"""

"""
Collect files with in a supplied directory. 
Final result should be a json sample file that is able to perform
analysis. With json will have data
 [date last accessed, size of file, path to the file, file name,
  and the extension]
"""
import os
from halo import Halo
from pathlib import WindowsPath
from save_doc import save_report_json
from file_inventroy import take_inventory_dir


def main(working_dir):
    with Halo(text='Searching Dir', spinner='dots'):
        # searches through directory supplied and return dictionary with file class
        dir_evaluation = take_inventory_dir(working_dir)

    # save json to the working directory
    save_report_json(dir_evaluation)


if __name__ == "__main__":
    # future will take a arg from terminal

    working_dir = r"S:\V2"
#    working_dir = r"F:"

    main(working_dir)
    
    
    ### -- SAVE JSON FILE ---
import csv
import json


def save_report_csv(dict_stat, current_work_dir):

    saved_dir_file_name = f"{current_work_dir}\\checks_TESTING.csv"

    with open(saved_dir_file_name, 'w', newline='') as csv_file:
        data_writer = csv.writer(
            csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for file_data in dict_stat:
            year = str(file_data.year_file_accessed())
            size = str(file_data.file_size_KB())
            path = file_data.file_path

            data_writer.writerow([year, size, path])

    print(saved_dir_file_name)


def save_report_json(working_list):

    # Serializing json
    json_object = json.dumps(working_list, indent=2)

    # Writing to sample.json
    with open(f"file_eval_save-full.json", "w") as outfile:
        outfile.write(json_object)

    print("file saved")

