"""
obtain the data for files need to analysis
"""
import os
from time import strftime, gmtime


class File_Data:
    def __init__(self, subdir, dirs, file_name):
        self.subdir = subdir
        self.dirs = dirs
        self.file_name = file_name
        self.file_path = self.subdir + os.sep + self.file_name

    def file_type_extension(self):
        return os.path.splitext(self.file_name)[1]

    def year_file_accessed(self):
        access_date_file = os.stat(self.file_path).st_mtime
        file_access_year = strftime("%Y", gmtime(access_date_file))
        return file_access_year

    def file_size_KB(self):
        return os.stat(self.file_path).st_size

    def __str__(self):
        return self.file_name
