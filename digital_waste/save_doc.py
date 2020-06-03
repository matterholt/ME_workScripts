"""
Created on Tue Jun  2 10:01:25 2020

@author: MATTERHOLT
"""
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


def save_report_json(working_list, dir_analysed):
    file_analyzed = "_".join(dir_analysed.split("/"))
    # Serializing json
    json_object = json.dumps(working_list, indent=2)

    # Writing to sample.json
    with open(f"file_inventory_{file_analyzed}.json", "w") as outfile:
        outfile.write(json_object)

    print("file saved")
