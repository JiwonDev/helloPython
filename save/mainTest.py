import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_toList(self):
        "toList 테스트 - 문자열 리스트로 변환이 잘 되는지 확인한다."
        answer = toList("1+2+3+4", "+")
        self.assertEquals(['1', '2', '3', '4'], answer)

    def test_toInt(self):
        "toInt 테스트 - 문자열 리스트가 숫자 리스트로 변환되는지 확인한다."
        answer = toInt(['1', '2', '3', '4'])
        self.assertEquals([1, 2, 3, 4], answer)

    def test_string_calculator(self):
        "문자열 계산기가 잘 동작하는지 확인한다."
        answer = string_calculator("1+2+3+4")
        self.assertEquals(10, answer)


if __name__ == '__main__':
    unittest.main()
