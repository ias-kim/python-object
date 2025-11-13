input_data = input()

row = int(input_data[1])
column = int(ord(input_data[0])) - ord('a') + 1

# 8개의 방향 수치
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
         (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0

for move in moves:

    x_row = row + move[0]
    x_column = column + move[1]
    
    if (x_row >= 1 and x_row <= 8 and x_column >= 1 and x_column <= 8):
        count += 1

print(count)
