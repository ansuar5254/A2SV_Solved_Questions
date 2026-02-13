matrix = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            move = abs(2-i) + abs(2-j)
            print(move)
            break
