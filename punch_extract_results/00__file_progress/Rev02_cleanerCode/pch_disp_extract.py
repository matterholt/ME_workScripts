# -*- coding: utf-8 -*-

import re

file_loc = r"/data/"
file_file = "data.pch"
document_to_extract = file_loc + file_file


def read_document(doc):
    with open(doc, 'r') as full_doc
    full_doc_string = full_doc.read()
    return full_doc_string


def find_regex_structure(re_pattern, full_doc):
    match_patterns = re.findall(re_pattern, full_doc)
    return match_patterns


def subcase_labels(doc_string):
    label_reg_pattern = r"\$LABEL\s*=\s+(.*)"
    subcase_label = find_regex_structure(label_reg_pattern, doc_string)
    return subcase_label


def subcase_displacement_value(doc_string):
    value_reg_pattern = r".110\W*G\s+(\S+)\s+(\S+)\s+(\S+)\s+"
    subcase_values = find_regex_structure(value_reg_pattern, doc_string)
    return subcase_values


def subcase_id(doc_string):
    subcase_reg_pattern = r"\$SUBCASE ID\W*(\d*)"
    subcase_id = find_regex_structure(subcase_reg_pattern, doc_string)


def direction_applied_direction():
    pass


def scrub_displacement():
    pass


def compile_data():
    # document, could be change
    document = read_document(document_to_extract)

    subcase_labels = subcase_labels(document)
    subcase_disp_values = subcase_displacement_value(document)
    subcase_ids = subcase_id(document)

    return ([subcase_labels, subcase_disp_values, subcase_ids])

compile_data()