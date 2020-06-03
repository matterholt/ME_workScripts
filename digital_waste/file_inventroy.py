
def take_inventory_dir(dir_path, file_requirements):

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
        "file_error": file_path_error,
        "review_files": review_file_list,
        "junk_files": junk_file_list,
        "other_files": other_file_list
    }
    return file_bundle


def parse_file_info(file):
    if "file_error" in file:
        del file["file_error"]

    doc_try = []

    for file_category in file.keys():
        data_stage = file[file_category]
        data_list = {'file_category': file_category, 'file_data': []}
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
