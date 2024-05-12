import unittest

from pi_log import logs


class TestLogs(unittest.TestCase):
    def test_set_app_logging(self):
        logs.set_app_root("DebugApp")
        log = logs.get_app_logger()
        self.assertEqual(log.name, "DebugApp")

    def test_set_app_logging_within_main(self):
        log = logs.getLogger(__name__, to_stdout=True, level="DEBUG")

        self.assertEqual(log.name, "__main__")
        log.setLevel("DEBUG")
        log.debug("Debug message")

    def test_set_app_logging_within_module(self):
        log = logs.log

        self.assertEqual(log.name, "pi_log.logs")
        log.setLevel("DEBUG")
        log.debug("Debug message")

if __name__ == "__main__":
    unittest.main()
