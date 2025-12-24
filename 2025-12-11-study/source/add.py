
# < 좋은 코드 >
def add(a, b):
    result = a + b
    print(result)

add(1,2)

# < 나쁜 코드 >
def number_three_print():
    result = 1 + 2
    print(result)

number_three_print()


# 문장 만들기
# ( 사람이름 )는 ( 물건 )을 깜빡하고 놓고 와서 ( 결과행위 ).
def 문장만들기(who, what, result):
    print(who + "는 " + what + "을 깜빡하고 놓고 와서 " + result + ".")

문장만들기("나", "지갑", "밥을 못먹는다")