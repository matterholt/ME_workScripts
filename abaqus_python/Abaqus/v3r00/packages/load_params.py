"""
using the .inp file to get load parameters, 
node, load direction, system type, 
"""
import re


def helper_regex_search(pattern, file):
    pattern = re.compile(pattern)
    item_search = pattern.search(file)
    if item_search:
        return item_search.group(1)
    else:
        # send to a log file for user
        print('item not found')


def load_system_applied(inp_file_sting):
    system_regex = re.compile(r"global=NO,")
    system_define = system_regex.search(inp_file_sting)
    if system_define:
        return 'LOCAL'
    else:
        return 'GLOBAL'


def node_load_applied(inp_file_string):
    node_pattern = r"NODE=(\d+)"
    node_define = helper_regex_search(node_pattern, inp_file_string)
    return node_define


def dof_load_applied(inp_file_string):
    dof_pattern = r"DOF=(\d+)"
    dof_define = helper_regex_search(dof_pattern, inp_file_string)
    return dof_define


def inp_load_parameters(file):
    system_type = load_system_applied(file)
    node_load = node_load_applied(file)
    direction_load = dof_load_applied(file)
    return [system_type, node_load, direction_load]
