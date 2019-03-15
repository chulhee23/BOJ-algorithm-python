a= int(input())

for i in range(1,a+1):
  print(' '*(i-1), end='')
  print('*'*(a-i+1))