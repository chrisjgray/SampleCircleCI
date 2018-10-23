import unittest
from HelloWorld import Hello
class TestCase(unittest.TestCase):
    def test_default_hello(self):
        hello = Hello()
        self.assertEqual(hello.message, 'Hello World')

if __name__ == '__main__':
    unittest.main()
