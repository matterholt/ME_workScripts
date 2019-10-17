import pytest
from v3r00.packages.dir_file_odbLoc import filter_odbfile, check_for_inp, ind_files_for_extraction


class Test_directory_file_ODBloc:
    def test_filter_odbfile(self):
        dir_list = ['a.odb', 'b.odb', 'c.inp', 'b.inp']
        assert filter_odbfile(dir_list) == ['a.odb', 'b.odb', ]

    def test_check_for_inp(self):
        dir_list = ['a.odb', 'b.odb', 'c.inp', 'b.inp']
        odb_list = ['a.odb', 'b.odb']
        assert check_for_inp(dir_list, odb_list) == ['b.odb']

    def test_find_files_for_extraction(self):
        dir_list = ['a.odb', 'b.odb', 'c.inp', 'b.inp']
        assert ind_files_for_extraction(dir_list) == ['b.odb']
