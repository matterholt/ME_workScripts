import pytest
from v3r00.packages.dir_file_odbLoc import filter_odbfile


class Test_directory_file_ODBloc:
    def test_filter_odbfile(self):
        dir_list = ['a.odb', 'b.odb', 'c.inp', 'd.inp']
        assert filter_odbfile(dir_list) == ['a.odb', 'b.odb', ]
