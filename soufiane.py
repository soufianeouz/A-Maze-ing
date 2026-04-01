from collections import deque

maze = [[11, 9, 5, 5, 3, 9, 5, 3, 13, 1, 5, 3, 9, 5, 3, 13, 5, 3, 9, 1, 7, 9, 5, 5, 3], [10, 12, 5, 3, 12, 6, 11, 12, 5, 6, 9, 6, 10, 11, 12, 5, 3, 10, 10, 12, 3, 12, 3, 9, 2], [12, 5, 5, 6, 9, 5, 4, 5, 1, 7, 8, 5, 6, 12, 5, 5, 2, 12, 4, 3, 12, 5, 6, 10, 10], [9, 5, 5, 3, 8, 3, 9, 5, 6, 15, 10, 15, 11, 15, 15, 15, 12, 3, 11, 10, 9, 3, 9, 6, 10], [10, 9, 3, 10, 10, 10, 10, 13, 3, 15, 14, 15, 8, 5, 7, 15, 9, 6, 12, 6, 10, 10, 10, 11, 10], [10, 14, 12, 6, 10, 10, 12, 5, 6, 15, 15, 15, 10, 15, 15, 15, 12, 3, 9, 3, 10, 12, 6, 10, 10], [8, 5, 5, 3, 10, 12, 5, 5, 5, 1, 7, 15, 10, 15, 13, 5, 3, 12, 6, 12, 6, 9, 3, 8, 6], [12, 7, 9, 2, 10, 9, 5, 5, 3, 12, 3, 15, 10, 15, 15, 15, 8, 5, 1, 5, 3, 10, 12, 6, 11], [9, 5, 6, 14, 12, 6, 9, 7, 10, 11, 10, 9, 2, 9, 1, 7, 10, 11, 10, 13, 2, 12, 5, 5, 2], [8, 5, 5, 5, 1, 5, 6, 9, 6, 10, 10, 10, 10, 10, 10, 9, 6, 10, 12, 3, 14, 9, 3, 9, 6], [12, 5, 5, 7, 12, 5, 5, 4, 5, 6, 12, 6, 12, 6, 12, 4, 5, 4, 7, 12, 5, 6, 12, 4, 7]]


if __name__ == "__main__":
    start = (0, 0)
    end = (3, 3)
    parents = {}
    
    to_visit = deque([start])
    visited = set([start])

while to_visit:
    x, y = to_visit.popleft()
    cell = maze[x][y]

    if (x, y) == end:
        break

    # 🔼 UP
    if not (cell & 1):
        nx, ny = x - 1, y
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            to_visit.append((nx, ny))
            parents[(nx, ny)] = (x, y)

    # ▶️ RIGHT
    if not (cell & 2):
        nx, ny = x, y + 1
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            to_visit.append((nx, ny))
            parents[(nx, ny)] = (x, y)

    # 🔽 DOWN
    if not (cell & 4):
        nx, ny = x + 1, y
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            to_visit.append((nx, ny))
            parents[(nx, ny)] = (x, y)

    # ◀️ LEFT
    if not (cell & 8):
        nx, ny = x, y - 1
        if (nx, ny) not in visited:
            visited.add((nx, ny))
            to_visit.append((nx, ny))
            parents[(nx, ny)] = (x, y)


if end not in parents:
    print("No path found")
else:
    list_path = deque()
    current = end

    while current != start:
        list_path.appendleft(current)
        current = parents[current]

    list_path.appendleft(start)
    print(list_path)
