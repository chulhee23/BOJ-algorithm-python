# 40.996%
# 문제
# 상근이는 영화 DVD 수집가이다. 상근이는 그의 DVD 콜렉션을 쌓아 보관한다.

# 보고 싶은 영화가 있을 때는, DVD의 위치를 찾은 다음 쌓아놓은 콜렉션이 무너지지 않게 조심스럽게 DVD를 뺀다. 영화를 다 본 이후에는 가장 위에 놓는다.

# 상근이는 DVD가 매우 많기 때문에, 영화의 위치를 찾는데 시간이 너무 오래 걸린다. 각 DVD의 위치는, 찾으려는 DVD의 위에 있는 영화의 개수만 알면 쉽게 구할 수 있다. 각 영화는 DVD 표지에 붙어있는 숫자로 쉽게 구별할 수 있다.

# 각 영화의 위치를 기록하는 프로그램을 작성하시오. 상근이가 영화를 한 편 볼 때마다 그 DVD의 위에 몇 개의 DVD가 있었는지를 구해야 한다.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 테스트 케이스의 개수는 100개를 넘지 않는다.

# 각 테스트 케이스의 첫째 줄에는 상근이가 가지고 있는 영화의 수 n과 보려고 하는 영화의 수 m이 주어진다. (1 ≤ n, m ≤ 100,000) 둘째 줄에는 보려고 하는 영화의 번호가 순서대로 주어진다.

# 영화의 번호는 1부터 n까지 이며, 가장 처음에 영화가 쌓여진 순서는 1부터 증가하는 순서이다. 가장 위에 있는 영화의 번호는 1이다. 

# 출력
# 각 테스트 케이스에 대해서 한 줄에 m개의 정수를 출력해야 한다. i번째 출력하는 수는 i번째로 영화를 볼 때 그 영화의 위에 있었던 DVD의 개수이다. 상근이는 매번 영화를 볼 때마다 본 영화 DVD를 가장 위에 놓는다.

n = int(input())
movieList=[]

watch=[]

real_answer=[]
for a in range(n):
    answer=[]
    tempList = []

    movie_number, num = map(int, input().split())
    
    for i in range(movie_number):
        tempList.append(i+1)

    movieList.append(list(tempList))
    watch.append(list(map(int, input().split()))) # 볼 영화들을 리스트로 생성
    for title in watch[a]:
        for movie in movieList[a]:
            if movie==title:
                temp = movieList[a].index(movie)
                answer.append(temp)
                movieList[a].pop(temp)
                movieList[a].insert(0, movie)

    real_answer.append(answer)

# 마지막 답을 출력해줘야 한다.
for ans in real_answer:
    for i in ans:
        print(i, end=' ')
    print()