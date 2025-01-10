import unittest
from unittest.mock import patch
import runpy


class TestMain(unittest.TestCase):

    @patch("src.render.Render")
    def test_main_if_clause(self, MockRender):
        runpy.run_path("main.py", run_name="__main__")
        MockRender.assert_called_once()
        MockRender.return_value.run.assert_called_once()

    @patch("src.render.Render")
    def test_main_no_clause(self, MockRender):
        runpy.run_path("main.py", run_name="__test__")
        MockRender.assert_not_called()
        MockRender.return_value.run.assert_not_called()


if __name__ == "__main__":
    unittest.main()
