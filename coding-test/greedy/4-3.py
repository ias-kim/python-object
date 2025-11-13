input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

moves = [ (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2) ]

count = 0
# 8가지 방향으로 이동가능 한지 확인
for move in moves:
    # 이동하고자 하는 위치 확인
    next_row = row + move[0]
    next_column = column + move[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1

print(count)