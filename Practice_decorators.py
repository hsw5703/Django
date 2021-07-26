# def decorator(func):
#     def decorated(input_text):
#         print("함수 시작")
#         func(input_text)
#         print("함수 끝")
#     return decorated
#
# @decorator
#
# def hello_world(input_text):
#     print("함수 시작")
#     print(input_text)
#     print("함수 끝")
#
# decorator(hello_world("Hello"))


def check_integer(func):
    def decorated(width, height):
        if width > 0 and height > 0:
            return func(width, height)
        else:
            raise ValueError("Input must be positive value")
    return decorated

@check_integer

def rect_area(width, height):
    return width * height
@check_integer
def tri_area(width, height):
    return 0.5 * width * height

#print(rect_area(0, 10))
print(tri_area(0, 10))

"""
그니까 rect_area(10,10) 이거 호출되는걸 풀면

f = check_integer(rect_area)
f()
이렇게 두줄로 나뉘게돼 

decorated()가 아닌 decorated만 쓰면 함수를 실행하는 게 아니라 함수의 위치를 가리키게 된다.

첫줄만 실행하면 f는 decorated 를 가리키게되고 그 아래에서 f()로 decorated를 호출하게됨!
그럼 이 decorated는 앞에 check_integer로 받은 rect_area 의 주소가 있응게 거기서 width랑 height를 가져올 수 있게되고 
ㅇㅇ 걍 저 코드대로 동작함 이건 조금 생각해봐야 되겠구먼.... 설명은 굿 좋았습니다
저기서 func() 를 호출하잖아 근데 func에는 아까 받은 rect_area가 있으니까 ㅇㅇ return width*height 가 동작하는거지
"""