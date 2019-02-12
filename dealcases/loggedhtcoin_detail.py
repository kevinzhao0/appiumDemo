# coding=utf-8

from Base.baseaction.unittestcase import UnitTestCase
from Base.baseaction.commonutils import login
from dealcase import DealCase
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

deal_case = DealCase()
yaml_path = PATH("../yamlcases/logged/htcoin_detail.yaml")


class Mine(UnitTestCase):
    def setUp(self):
        self.my_log.log_start_line()

    def tearDown(self):
        self.my_log.log_end_line()

    @classmethod
    def setUpClass(cls):
        super(Mine, cls).setUpClass()

    def test_my_coin(self):
        u"""我的海豚币-明细"""
        # login(self.driver)`
        deal_case.deal_case(self, self.driver, yaml_path, self.my_log)

    @classmethod
    def tearDownClass(cls):
        super(Mine, cls).tearDownClass()

# if __name__=="__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(Mine)
#     unittest.TextTestRunner(verbosity=2).run(suite)
