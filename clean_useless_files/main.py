"""
Remove listed files that are not needed in dirs


"""
import os
import timeit
import datetime

from time import strftime, gmtime


def print_time_took(time):
    """ print the correct time unit for the execution code """
    if time > 60000000:
        print(str(round(time/60000000, 2)) + " Minutes")

    if time > 1000000:
        print(str(round(time / 1000000, 2)) + " Seconds")

    else:
        print(str(round(time, 2)) + " MicroSeconds")


def year_file_create(file):
    access_date_file = os.stat(file).st_mtime
    file_access_year = strftime("%Y", gmtime(access_date_file))
    return file_access_year


def calculate_file_size(file):
    file_KB_size = os.stat(file).st_size
    return file_KB_size


def terminal_print(specs):
    for key, val in specs.items():
        print(key, val)


def search_dir(dir_path, inputs_bond):

    search_info = {}

    access_date = {}
    extension_count = {}

    accumulated_file_size = 0
    files_path_error = 0

    for subdir, dirs, files in os.walk(dir_path):

        for file_name in files:

            try:
                file_path = subdir + os.sep + file_name

                for extensions in inputs_bond.extension_no_need:
                    if file_path.endswith(extensions):

                        # extension count
                        extension_count[extensions] = extension_count.get(
                            extensions, 0) + 1

                        # find the date the file was last accessed
                        file_access_last = year_file_create(file_path)
                        access_date[file_access_last] = access_date.get(
                            file_access_last, 0) + 1

                        # count the file size
                        file_size = calculate_file_size(file_path)
                        accumulated_file_size += file_size

            except FileNotFoundError:
                # search_info["path_ng"] += search_info.get("path_ng", 0)+1
                files_path_error += 1

    search_info.update(file_path=dir_path)
    search_info.update(Kb_size=accumulated_file_size)  # convert to GB
    search_info.update(failed_path=files_path_error)
    search_info.update(access_date)
    search_info.update(extension_count)

    return search_info


def main():
    boundaries = {
        "extension_no_need": [".html", ".out", ".res", ".stat",
                              ".mesg", ".mvw"],
        "extension_remove_old": [".op2", ".odb", ".hyp", ".h3d"],
        "current_date": datetime.datetime
    }
    # correct / better way to parse the path os.path.join ??
    # raw_dir_path = r"F:"
    raw_dir_path = r"S:/v2"

    found_files_info = search_dir(raw_dir_path, boundaries)

    terminal_print(found_files_info)

    return found_files_info


if __name__ == "__main__":
    timeit.timeit(main, number=1)
