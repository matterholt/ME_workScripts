"""
Remove listed files that are not needed in dirs

"""
import os
#import timeit
import datetime


from time import strftime, gmtime, sleep

def split_join_string(dir_path):
    path_sting = dir_path.split(':\\')
    s = '-'
    return s.join(path_sting)
    

def save_data_csv(dict_stat, current_date):
    dir_check = split_join_string(dict_stat['file_path'])
    
    current_work_dir = os.getcwd()
    saved_dir_file_name = f"{current_work_dir}\\checks_{dir_check}_{current_date}.csv"
    
    try:
        with open(saved_dir_file_name,'w') as csv_file:

            for [key, val] in dict_stat.items():
                csv_file.write("%s,%s\n"%(key,val))
            
            
            print(f"\nCSV_Saved: \n{saved_dir_file_name}\n")
            
    except IOError:
        print("I/O error")
        
    return

def print_time_took(time):
    """ print the correct time unit for the execution code """
    print(time)
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


def file_size_KB(file):
    file_KB_size = os.stat(file).st_size
    return file_KB_size


def terminal_print(specs):
    print("Rundown of Search")
    for key, val in specs.items():
        sleep(0.3)
        print(f"{key} -> {val}")


def remove_files(file):
    try:
        print(f"REMOVED -> /N{file} ")
        os.remove(file)
    except PermissionError:
        print("Error while deleting file ", file)
            
    return
    

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
                
                
                # TODO-> check files that are 2 or so years old, 
                # TODO-> check duplicate files 
                for extensions in inputs_bond["extension_no_need"]:
                    """ 
                    Reviews the file extension, if found in list will document 
                    specs and proced to remove from the directory
                    """
                    if file_path.endswith(extensions):

                        # extension count
                        extension_count[extensions] = extension_count.get(
                            extensions, 0) + 1

                        # find the date the file was last accessed
                        file_access_last = year_file_create(file_path)
                        access_date[file_access_last] = access_date.get(
                            file_access_last, 0) + 1

                        # count the file size
                        file_size = file_size_KB(file_path)
                        accumulated_file_size += file_size
                        
                        # REMOVE FILES ONCE DATA IS STORED
                        if inputs_bond['want_to_remove'] :
                            print('will remove!!!')
                            remove_files(file_path)


            except FileNotFoundError:
                files_path_error += 1

    search_info.update(file_path=dir_path)
    search_info.update(GB_size= round(accumulated_file_size/1000000000,2))  # convert to GB
    search_info.update(failed_path=files_path_error)
    
    search_info.update(extension_count)
    search_info.update(access_date)
    
    return search_info


def main():
    
    now_date_time = datetime.datetime.now()
    date_check = now_date_time.strftime("%Y-%m-%d")
    
    boundaries = {
        "want_to_remove" : False,
        "extension_no_need": [".html", ".out", ".res", ".stat",
                              ".mesg", ".mvw"],
        "extension_remove_old": [".op2", ".odb", ".hyp", ".h3d"]
    }
    

    raw_dir_path = r"F:"
#    raw_dir_path = r"S:/v2"

    found_files_info = search_dir(raw_dir_path, boundaries)
    terminal_print(found_files_info)
    save_data_csv(found_files_info,date_check)




    return found_files_info


if __name__ == "__main__":
    main()
#    script_time = timeit.timeit(main, number=1,globals=globals())
#    print_time_took(script_time)
