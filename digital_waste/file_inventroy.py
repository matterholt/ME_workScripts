import os
from file_class import File_Data


def take_inventory_dir(dir_path):

    file_path_error = 0

    default_file = []

    for subdir, dirs, files in os.walk

(dir_path):
        for file_name in files:
            try:
                file_specs = File_Data(subdir, dirs, file_name)
                data = {
                  

  "name": file_specs.file_name,
                    "year": file_specs.year_file_accessed(),
                    "size": file_specs.file_size_KB(),
                  

  "path": file_specs.file_path,
                    "extension": file_specs.file_type_extension()
                }
                default_file.append(data)

         

   except FileNotFoundError:
                file_path_error += 1
    print(f"{file_path_error} paths are NG")

    return default_file

