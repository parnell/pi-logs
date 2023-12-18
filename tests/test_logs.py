import os
import unittest

from pi_log import logs


class TestLogs(unittest.TestCase):
    def test_set_app_logging(self):
        logs.set_app_root("DebugApp")
        log = logs.get_app_logger()
        self.assertEqual(log.name, "DebugApp")




if __name__ == "__main__":
    unittest.main()
