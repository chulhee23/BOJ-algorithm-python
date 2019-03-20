# 각 자리의 숫자 구하기
x = int(input())
thousands = x // 1000
hundreds = x // 100 %10
tens = x // 10 % 10
units = x % 10

print(thousands)
print(hundreds)
print(tens)
print(units)