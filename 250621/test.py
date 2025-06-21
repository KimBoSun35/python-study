def hello():
    print("Hello")
    

def holjak(num):
    result=""
    if num%2==0:
        result="짝수"
    elif num%2==1:
        result="홀수"
    else:
        result="입력받은 숫자가 정수가 아닙니다."
    return result
