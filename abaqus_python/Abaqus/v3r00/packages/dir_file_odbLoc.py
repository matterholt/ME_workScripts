"""
search through a supplied directory.
Using Regex to search odb
all odb should have a .inp file that has same name
"""
import re


def filter_odbfile(all_file_dir):
    all_odb_dir = []
    pattern_odb = re.compile(r".*\.odb")

    for file_name in all_file_dir:
        odb_file = pattern_odb.match(file_name)
        if odb_file:
            all_odb_dir.append(file_name)
        else:
            # send to log for user
            pass
    return all_odb_dir


def check_for_inp(all_file_dir, odb_files):
    filter_odbs = []
    for odb_file in odb_files:
        inp_file = odb_file[0:-3] + "inp"
        for file in all_file_dir:
            if inp_file == file:
                filter_odbs.append(odb_file)
            else:
                pass
                # send to log for user
    return filter_odbs


def find_files_for_extraction(all_files):
    odb_file_in_dir = filter_odbfile(all_files)
    odb_checkFor_inp = check_for_inp(all_files, odb_file_in_dir)
    return odb_checkFor_inp
