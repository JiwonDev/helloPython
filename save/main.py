"""
# 1. 문자열 덧셈 계산기 구현
- '3+4+5' 를 입력하면 int 형으로 결과를 반환한다.
- '3+' 처럼 처리할 수 없는 경우 0을 반환한다.
"""

# 문자열 "1+2+3+4"을 +를 기준으로 문자열 리스트["1","2","3","4"]로 만든다.
from typing import List


def toList(input_string: str, delimiter: str = '+') -> list[str]:
    return input_string.split(delimiter)


def toInt(digits: list[str]) -> list[int]:
    result_list: list[int] = []
    for x in digits:
        result_list.append(int(x))
    return result_list


def string_calculator(input_string: str) -> int:
    # 2. 입력받은 문자열에서 숫자를 리스트로 나눈다. (단 delimiter를 구분자로 사용해서)
    str_digit_list = toList(input_string, "+")

    # 3. 문자리스트를 숫자리스트로 변경한다.
    int_list = toInt(str_digit_list)

    # 4. int 형 리스트를 덧셈을 한다.
    summary = sum(int_list)

    return summary


def main():
    # input_string = input("입력하세요 : ")
    # 문자열 계산기를 구현하거라
    answer = string_calculator("1+2+3+4")  # 메인 시작
    "1+1+2+3"
    print(toList("1+1+2+3"))
    print(f"답은 {answer} 입니다")


# if : 이 스크립트 파일(main.py)을 직접 실행한 경우 True.
if __name__ == '__main__':
    main()

