# 문제
# 백설 공주와 난쟁이 N명과 함께 숲 속에 살고 있다. 난쟁이는 매일 광산에 일하러가고, 백설 공주는 그동안 페이스북을 하고 있다.

# 매일 아침 난쟁이는 한 줄로 휘파람을 불면서 광산으로 출근을 한다. 백설 공주는 그 주변을 돌아다니면서 난쟁이들 사진을 찍는다.

# 난쟁이가 광산에 들어가면, 백설 공주는 다시 집으로 돌아간다. 집으로 돌아가면서 찍은 사진 중에 페이스북에 올릴 예쁜 사진을 고른다. 각 난쟁이는 모두 모자를 쓰고 있다. 모자의 색상은 총 C가지가 있다. 사진에 찍힌 난쟁이가 쓰고 있는 모자의 색상 중 절반보다 많은 색이 같은 색이라면 예쁜 사진이다. 즉, 사진에 난쟁이가 K명 찍혀있고, K/2보다 많은 난쟁이의 모자 색이 같다면 예쁜 사진이다.

# 백설공주가 찍은 사진 M개와 각 사진에 찍힌 난쟁이가 주어졌을 때, 예쁜 사진인지 아닌지를 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 난쟁이의 수 N과 모자 색상의 수 C가 주어진다. (3 ≤ N ≤ 300,000, 1 ≤ C ≤ 10,000)

# 둘째 줄에는 각 난쟁이가 쓰고 있는 모자의 색상이 줄을 서 있는 순서대로 주어진다.

# 셋째 줄에는 사진의 수 M이 주어진다. (1 ≤ M ≤ 10,000)

# 다음 M개 줄에는 두 정수 A와 B가 주어진다. (1 ≤ A ≤ B ≤ N) 이 줄은 사진의 정보를 의미하고, A번째 난쟁이부터 B번째 난쟁이까지 사진에 찍혔다는 뜻이다.

# 출력
# 출력은 총 M 줄이다. 각 사진이 예쁘지 않다면 "no"를 출력하고, 예쁘다면 "yes X"를 출력한다. 예쁜 사진인 경우에 X는 사진에 절반이 넘는 모자의 색상이다.

number, color = map(int, input().split())
# 모자의 색상을 숫자로 준다.
hat = list(map(int, input().split()))
photo = int(input())
answer=[]

for i in range(photo):
    a, b = map(int, input().split())
    start = a-1
    end = b-1
    temp = hat[start:end+1] # start와 end 포함한 리스트로 슬라이싱
    max=0
    
    for item in temp:
        if max <= temp.count(item):
            max = temp.count(item)
            maxColor = item
    
    if len(temp)/2 < max:
        answer.append(maxColor)
    else:
        answer.append('no')

for i in answer:
    if type(i)==int:
        print('yes', i)
    else:
        print(i)




