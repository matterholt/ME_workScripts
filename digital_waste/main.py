
import os
from save_doc import save_report_json
from file_inventroy import take_inventory_dir, parse_file_info


def main(working_dir, file_requirements):

    dir_evaluation = take_inventory_dir(working_dir, file_requirements)
    working_data = parse_file_info(dir_evaluation)
    save_report_json(working_data)


if __name__ == "__main__":
    #    working_dir = r"F:"
    working_dir = r"S:\V2\mesh"

    file_requirements = {
        "junk_file": [".html", ".out", ".res", ".stat", ".sta", ".f04",
                      ".mesg", ".mvw"],
        "review_file": ['.hm', '.inp', '.fem', '.CATAnalysis', 'CATPart',
                        '.avi', 'lms']
    }

    main(working_dir, file_requirements)
