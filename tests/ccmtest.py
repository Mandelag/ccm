import os
from unittest import TestCase


class Tester(TestCase):

    check_log_errors = True

    def __init__(self, *argv, **kwargs):
        super(Tester, self).__init__(*argv, **kwargs)

    def setUp(self):
        self.check_log_errors = True

    def tearDown(self):
        if hasattr(self, 'cluster'):
            try:
                if self.check_log_errors:
                    for node in self.cluster.nodelist():
                        self.assertListEqual(node.grep_log_for_errors(), [])
            finally:
                test_path = self.cluster.get_path()
                self.cluster.remove()
                if os.path.exists(test_path):
                    os.remove(test_path)
