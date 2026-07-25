from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    answer = 0

    def bfs():
        nonlocal answer

        q = deque([(0,0)])
        visited[0][0] = True

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        maps[nx][ny] = maps[x][y] + 1

    bfs()
    if not visited[n-1][m-1]:
            return -1
        
    return maps[n-1][m-1]