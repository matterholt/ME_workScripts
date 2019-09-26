# -*- coding: utf-8 -*-
from local_packages.read_file import read_doc


def main():
    str_test = "can you work??"
    test = read_doc(str_test)
    print(test)


if __name__ == "__main__":
    main()
