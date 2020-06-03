"""
Unit testing for the load parameters
"""
import pytest
from ..packages.load_params import load_system_applied, node_load_applied, helper_regex_search, dof_load_applied, inp_load_parameters


class Test_Load_Params:

    @pytest.fixture(scope="module")
    def base_string(self):
        local_applied = r"""*Node Output, global=NO, nset=ACTUATOR
        MONITOR,DOF=3,NODE=111
        """
        return local_applied

    def test_helper_regex_search(self, base_string):
        node_pattern = r"NODE=(\d+)"
        assert helper_regex_search(node_pattern, base_string) == '111'

    def test_load_localSystem(self, base_string):
        assert load_system_applied(base_string) == 'LOCAL'
        assert load_system_applied(base_string) != 'GLOBAL'

    def test_node_load_applied(self, base_string):
        assert node_load_applied(base_string) == '111'

    def test_dof_load_applied(self, base_string):
        assert dof_load_applied(base_string) == '3'

    def test_inp_load_parameters(self, base_string):
        assert inp_load_parameters(base_string) == ['LOCAL', '111', '3']
