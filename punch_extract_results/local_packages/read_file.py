"""
Read file module is script to extract all file

"""


def read_doc(doc):
    with open(doc, 'r') as doc_list:
        full_doc_str = doc_list.read()
        return full_doc_str
