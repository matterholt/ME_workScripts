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
