import pytest
from ..packages.dir_file_odbLoc import filter_odbfile, check_for_inp, find_files_for_extraction


class Test_directory_file_ODBloc:

    @pytest.fixture
    def file_list(self):
        dir_list = ['a.odb', 'b.odb', 'c.inp', 'b.inp']
        return dir_list

    def test_filter_odbfile(self, file_list):
        assert filter_odbfile(file_list) == ['a.odb', 'b.odb', ]

    def test_check_for_inp(self, file_list):
        odb_list = ['a.odb', 'b.odb']
        assert check_for_inp(file_list, odb_list) == ['b.odb']

    def test_find_files_for_extraction(self, file_list):
        assert find_files_for_extraction(file_list) == ['b.odb']
