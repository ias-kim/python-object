# n, m, k 문자열 입력
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입려받은 수들 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 가장 작은 수

count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first
result += (m - count) * second

print(result)