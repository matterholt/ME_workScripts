"""
first attempt on code
"""

import re
import math

label_list = []
subcase_list = []
value_list = []

file_loc = './test'
file_name = 'abc.pch'

with open (file_loc + file_name, 'r') as reader:
    label_pattern = re.compile(r"\$LABEL\s*=\s+(.*)")
    value_pattern = re.compile(r".*110\W*G\s+(\S+)\s+(\S)\s+(\S)\s+")
    subcase_pattern = re.compile(r"\$SUBCASE ID\W+(\d*)")
    for line in reader:
        label_result = label_pattern.match(line)
        value_result = value_pattern.match(line)
        subcase_result = subcase_pattern.match(line)
        if label_result:
            label_list.append(label_result.group[1])
        elif subcase_result:
            subcase_list.append(subcase_result.group(1))
        elif value_result:
            value_list.append(value_result.groups())

def combine_data(label, subID, vals):
    full_doc = []

    def get_XYZ_direction (index,index_of_input):
        direction_determine = int(index[1][-1])
        dir_value = math.fabs(float(vals[index_of_input][direction_determine]))
        return dir_value

    for i in enumerate(subID):
        index_of_input = i[0]

        subcase_label = label[index_of_input]
        subcase_ID = int(subcaseID[index_of_input])
        load_dir_value = get_XYZ_direction(i,index_of_input)

        build = [subcase_label,subcase_ID,load_dir_value]
        full_doc.append(build)
        
    return full_doc