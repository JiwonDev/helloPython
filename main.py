import math
from typing import Union

def main():
    cal_arthmetic(input())
    
def cal_arthmetic(input_str:str) -> Union[int,float]:
    numbers = []
    operators = []
    st = -1
    operator_flag = False 
    for idx, input_char in enumerate(input_str):
        print(input_char,"-", input_char.isdigit())
        if not input_char.isdigit(): # in "0123456789" 로 구현해도 될 거 같은데, 일단 isdigit에서 error가 없어서 naive 구현 했습니다
            if not operator_flag:
                print("잘못된 연산이 입력으로 들어왔습니다.")
                return math.inf
            else:
                operator_flag = False 
                numbers.append(int(input_str[st+1:idx]))
                operators.append(input_char)
                print(st, idx,"-",input_str[st+1:idx], "-숫자의 범위")
                st = idx
        else:
            operator_flag = True
    numbers.append(int(input_str[st:]))
    if len(numbers) - 1 != len(operators):
        print("연산자와 숫자의 갯수가 맞지 않습니다.") 
        return math.inf
    tmp = numbers[0]
    for number, operator in zip(numbers[1:],operators):
        if operator =='+':
            tmp = tmp + number
        elif operator =='-':
            tmp = tmp - number
        elif operator =='*':
            tmp = tmp * number
        elif operator =='/':
            tmp = tmp // number
    print(tmp, "-연산결과입니다")
    return tmp  
        

if __name__ == '__main__':
    main()