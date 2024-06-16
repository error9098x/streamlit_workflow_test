# test_app.py
import unittest
from streamlit_app import main

class TestStreamlitApp(unittest.TestCase):
    def test_main(self):
        try:
            main()
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, f"Exception occurred: {e}")

if __name__ == "__main__":
    unittest.main()
