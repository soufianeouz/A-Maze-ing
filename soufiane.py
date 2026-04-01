from collections import deque


def bfs_algorithm(maze: list[list[int]],
                  start: tuple[int, int],
                  end:tuple[int, int]) -> list[tuple[int, int]]:
    

    if start == end:
        return [start]
    
    parents = {}
    
    to_visit = deque([start])
    visited = set([start])

    while to_visit:
        x, y = to_visit.popleft()
        cell = maze[x][y]

        if end in visited:
            break

        # 🔼 UP
        if not (cell & 1):
            nx, ny = x - 1, y
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    to_visit.append((nx, ny))
                    parents[(nx, ny)] = (x, y)

        # ▶️ RIGHT
        if not (cell & 2):
            nx, ny = x, y + 1
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    to_visit.append((nx, ny))
                    parents[(nx, ny)] = (x, y)

        # 🔽 DOWN
        if not (cell & 4):
            nx, ny = x + 1, y
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    to_visit.append((nx, ny))
                    parents[(nx, ny)] = (x, y)

        # ◀️ LEFT
        if not (cell & 8):
            nx, ny = x, y - 1
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    to_visit.append((nx, ny))
                    parents[(nx, ny)] = (x, y)


    if end not in visited:
        return []
    else:
        list_path = deque()
        current = end

        while current != start:
            list_path.appendleft(current)
            current = parents[current]

        list_path.appendleft(start)
        return list(list_path)