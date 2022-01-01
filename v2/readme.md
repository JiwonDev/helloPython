# 1. 문자열 덧셈 계산기 구현
- '3+4+5' 를 입력하면 int 형으로 결과를 반환한다.
- '3+' 처럼 처리할 수 없는 경우 0을 반환한다.

# 2. main 메서드 테스트를 개선하기
- Production 코드와 Test 코드가 합쳐져있다.
- main을 다른 파일로 분리하자

# 3. 문자열 뺄셈, 나눗셈, 곱셈 기능추가
- 한 번에 메소드 하나에만 집중하기. 복잡도를 낮추기
- 연산자 우선순위는 고려하지않는다. 순서대로 처리한다.
- 0으로 나눴다면 "0으로 나눴습니다"를 출력하고 예외를 반환한다.