import sys
input = sys.stdin.readline

digit = int(input()) # 몇자리 수인지 입력

ans=[0,9,17]

units=[0,1,2,3,4,5,6,7,8,9]

number=123

unit= number%10

if unit==0:
#0은 1을 끝에 갖는다

elif (unit>0 and unit<9):
# 1~8은 2개의 가짓수 가질수 있음

else:
# 9는 한가지 생성