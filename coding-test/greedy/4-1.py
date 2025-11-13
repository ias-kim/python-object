n = int(input())
input = input().split()
x, y = 1,1

mv_x = [0, 0, -1, 1]
mv_y = [-1, 1, 0, 0]
space = ['L', 'R', 'U', 'D']

for move in input:
    nx, ny = 0, 0
    for i in range(len(space)):
        if (move == space[i]):
            nx += x + mv_x[i]
            ny += y + mv_y[i]
    
    if (nx < 1 or ny < 1 or nx > n or ny > n):
        continue

    x, y = nx, ny
print(x, y)