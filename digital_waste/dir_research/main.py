"""
Script to obtain info on the file within a given directory. Data will be exported as a csv file
"""

import os
from time import sleep


def terminal_print_dict(spec):
    """
    Nice and slowly print the dictionary info to the terminal. 
    will also print the highest value first
    """
    sort_dict = sorted(spec.items(), key=lambda item: item[1], reverse=True)
    print("--RUNDOWN--")
    for key, val in sort_dict:
        sleep(0.2)
        print(f"{key}-->{val}")


def take_inventory_dir(dir_path):
    """
    cycle through a directory searching for files
    """
    file_count_inventory = {}
    file_size_inventroy = {}

    file_path_error = 0

    for subdir, dirs, files in os.walk(dir_path):
        for file_name in files:

            file_path = subdir + os.sep + file_name

            inventory_extension = os.path.splitext(file_name)[1]

            file_count_inventory['total'] = file_count_inventory.get(
                'total', 0) + 1
            file_count_inventory[inventory_extension] = file_count_inventory.get(
                inventory_extension, 0) + 1

            try:
                extension_size = os.stat(file_path).st_size

                file_size_inventroy['total'] = file_size_inventroy.get(
                    'total', 0) + extension_size
                file_size_inventroy[inventory_extension] = file_size_inventroy.get(
                    inventory_extension, 0) + extension_size

            except FileNotFoundError:
                file_path_error += 1

    terminal_print_dict(file_count_inventory)
    terminal_print_dict(file_size_inventroy)


if __name__ == "__main__":
    working_dir = "/Users/matterholt/Projects"
    take_inventory_dir(working_dir)
