import unittest

from main import helloworld


class MainTest(unittest.TestCase):
    def test_helloworld(self):
        ret = helloworld()
        self.assertEqual(ret, "Hello World!")


if __name__ == "__main__":
    unittest.main()
