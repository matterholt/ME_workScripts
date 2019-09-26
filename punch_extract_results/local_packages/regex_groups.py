# -*- coding: utf-8 -*-
"""
M.Atterholt
2019.25.09

using regex to find the info located in the punch file
"""
import re


def find_regex_structure(re_pattern, full_doc):
    match_pattern = re.findall(re_pattern, full_doc)
    return match_pattern


def subcase_labels(doc_string):
    """
    label_reg_pattern = r"\$LABEL\s*=\s+(.*)"
    subcase_label = find_regex_structure(label_reg_pattern, doc_string)
    """
    return doc_string


def subcase_displacement_value(doc_string):
    value_reg_pattern = r".110\W*G\s+(\S+)\s+(\S+)\s+(\S+)\s+"
    subcase_values = find_regex_structure(value_reg_pattern, doc_string)
    return subcase_values


def subcase_id(doc_string):
    subcase_reg_pattern = r"\$SUBCASE ID\W*(\d*)"
    subcase_id = find_regex_structure(subcase_reg_pattern, doc_string)


def compile_data(pch_string):
    sub_label = subcase_labels(pch_string)
    sub_disp_value = subcase_displacement_value(pch_string)
    sub_ids = subcase_id(pch_string)
    return [sub_label, sub_disp_value, sub_ids]
