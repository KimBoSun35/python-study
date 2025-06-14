#sys라는 python package.module를 import
import sys

name= sys.argv[1]
print(" 저의 이름은"+name+"입니다.")

def plus_one(a):
    # 함수 내부 기능
    result = a + 1
    # 반환값(Output)
    return result

plus_one(1)