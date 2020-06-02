"""
Remove listed files that are not needed in dirs

"""
import os
import csv
from time import strftime, gmtime


class File_data:
    def __init__(self, subdir, dirs, file_name):
        self.subdir = subdir
        self.dirs = dirs
        self.file_name = file_name
        self.file_path = self.subdir + os.sep + self.file_name

    def file_extension_type(self):
        return os.path.splitext(self.file_path)

    def access_file_year(self):
        access_date_date = os.stat(self.file_path).st_mtime
        file_year = strftime("%Y", gmtime(access_date_date))
        return file_year

    def size_file_KB(self):
        return os.stat(self_path).st_size

    def __str__(self):
        return self.file_name


def take_inventory_dir(dir_path, file_requirements):

    file_path_error = 0

    other_files = []
    questionable_files = []
    junk_files = []

    for subdir, dirs, files in os.walk(dir_path):
        for file_name in files:
            try:
                file_spec = File_data(subdir, dirs, file_name)
                file_type_extension = file_spec.file_extension_type()

                if file_type_extension in file_requirements["review"]:
                    questionable_files.append(file_spec)
                elif file_type_extension in file_requirements["junk"]:
                    questionable_files.append(file_spec)
                else:
                    other_files.append(file_spec)
            except FileNotFoundError:
                file_path_error += 1

    # not sure if most efficient but it works ??
    file_bundle = {
        "file_error": file_path_error,
        "questionable": questionable_files,
        "junk": junk_files,
        "other": other_files
    }
    return file_bundle


def main():

    now_date_time = datetime.datetime.now()
    date_check = now_date_time.strftime("%Y-%m-%d")

    boundaries = {
        "junk_file": [".html", ".out", ".res", ".stat",
                      ".mesg", ".mvw"],
        "review_file": [".op2", ".odb", ".hyp", ".h3d"]
    }

    raw_dir_path = r"F:"
    dir_evaluation = take_inventory_dir(raw_dir_path, boundaries)


"""
lets open the possibility to add some libs
Bokeh, or some other data vis
"""


if __name__ == "__main__":
    main()
