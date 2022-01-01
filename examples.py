import unittest
from typing import Callable, Any
from v1.main import *


# command line에서 실행하는 방법
# python -m unittest v2.MyTestCase
# python -m unittest -v test_module.TestClass.test_method
class MyTestCase(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def setUp(self):
        # self.widget = Widget('The widget')
        pass

    @unittest.skip("demonstrating skipping")
    def tearDown(self):
        # self.widget.dispose()
        pass

    def test_something(self):
        """ Hello World"""
        name: str = "test String"
        string_calculator(name)
        self.assertEqual(name, "test String")

    def test_exception(self):
        raise_function: Callable[[Any], float] = lambda x: 1 / 0

        with self.assertRaises(ZeroDivisionError):
            raise_function(3)

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    def test_split(self):
        s = 'hello world'

        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string

        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
