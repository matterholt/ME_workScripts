"""
Collect files with in a supplied directory. 
Final result should be a json sample file that is able to perform
analysis. With json will have data
 [date last accessed, size of file, path to the file, file name,
  and the extension]
"""
import os
from pathlib import WindowsPath
from save_doc import save_report_json
from file_inventroy import take_inventory_dir, parse_file_info


def main(working_dir):

    # searches through directory supplied and return dictionary with file class
    dir_evaluation = take_inventory_dir(working_dir)

    # parse the class object into a dictionary to allow save able json
    working_data = parse_file_info(dir_evaluation)

    # save json to the working directory
    save_report_json(working_data, working_dir)


if __name__ == "__main__":
    # future will take a arg from terminal

    # working_dir = r"/Users/matterholt/test"
    # working_dir = WindowsPath(r"S:\V2\mesh")

    file_requirements = {
        "junk_file": [".html", ".out", ".res", ".stat", ".sta", ".f04",
                      ".mesg", ".mvw"],
        "review_file": ['.hm', '.inp', '.fem', '.CATAnalysis', 'CATPart',
                        '.avi', 'lms']
    }

    main(working_dir)
