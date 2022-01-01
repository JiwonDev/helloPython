def token_extractor(input_exp: str) -> list:
    return list(input_exp)


def toInt(digits: list) -> list:
    return list(map(int, digits))


def isOperator(token: str) -> bool:
    operators = ['+', '-', '*', '/']
    if token in operators:
        return True
    return False


def input_validator(tokens: list) -> bool:
    # 1. operator로 token이 시작하고 끝나면 안된다.
    # 2. digit과 operator가 교차되며 등장해야한다.
    # TODO: operator와 digit을 판단하는 함수가 필요함.
    if isOperator(tokens[0]) or isOperator(tokens[-1]) or len(tokens) < 2:
        return False

    isprevoperator = False

    for tmp_token in tokens[1:]:
        tmp_operator = isOperator(tmp_token)
        if isprevoperator == tmp_operator:
            return False
        isprevoperator = tmp_operator

    return True


def token_seperator(tokens: list) -> list:
    digits = []
    operators = []

    for tmp_token in tokens:
        if isOperator(tmp_token):
            operators.append(tmp_token)
        else:
            digits.append(tmp_token)

    return digits, operators


def calculate_operators(prev_num: int, now_num: int, operator: str) -> int:
    ret = None

    if operator == '+':
        return prev_num + now_num
    elif operator == '-':
        return prev_num - now_num
    elif operator == '*':
        return prev_num * now_num
    elif operator == '/':
        return prev_num // now_num


def calculate(digits: list, operators: list) -> int:
    prev_num = digits[0]
    for idx, now_num in enumerate(digits[1:]):
        prev_num = calculate_operators(prev_num, now_num, operators[idx])

    return prev_num


def plus_calculator(input_exp: str) -> int:
    # TODO: input_exp Digit과 Operator로 나눔.
    tokens: list = token_extractor(input_exp)

    # TODO: input_exp가 수식으로서 괜찮은지 판단해야함.
    validation: bool = input_validator(tokens)
    if validation is False:
        return None

    digits, operators = token_seperator(tokens)

    # TODO: Digit를 int형으로 바꿈(Digit들만)
    digits = toInt(digits)

    output = calculate(digits, operators)
    # TODO: Digit과 Operator를 이용해 연산을 진행한다
    return output


def main():
    print(plus_calculator('3+4+5') == 12)
    print(plus_calculator('3-5-2') == -4)
    print(plus_calculator('3+7+6') == 16)
    print(plus_calculator('1+2') == 3)
    print(plus_calculator('1') == 1)


if __name__ == '__main__':
    main()
