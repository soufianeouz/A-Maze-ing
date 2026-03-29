import random

def init_maze(width, height):
    """Creates a grid and a visited map."""
    grid = [[15 for _ in range(width)] for _ in range(height)]
    visited = [[False for _ in range(width)] for _ in range(height)]
    return grid, visited

def apply_42_stamp(visited, width, height):
    """Marks coordinates for '4' and '2' as visited."""
    digit_four = [
        (0, 0), (2, 0),
        (0, 1), (2, 1),
        (0, 2), (1, 2), (2, 2),
        (2, 3),
        (2, 4)
    ]
    digit_two = [
        (0, 0), (1, 0), (2, 0),
        (2, 1),
        (0, 2), (1, 2), (2, 2),
        (0, 3),
        (0, 4), (1, 4), (2, 4)
    ]

    if width < 7 or height < 5:
        return

    x_offset = (width - 7) // 2
    y_offset = (height - 5) // 2

    # Apply the '4'
    for x, y in digit_four:
        visited[y_offset + y][x_offset + x] = True

    for x, y in digit_two:
        visited[y_offset + y][x_offset + x + 4] = True

def get_unvisited_neighbors(x, y, width, height, visited):
    neighbors = []
    if y > 0 and not visited[y-1][x]:
        neighbors.append((x, y-1, 1, 4))
    if y < height - 1 and not visited[y+1][x]:
        neighbors.append((x, y+1, 4, 1))
    if x < width - 1 and not visited[y][x+1]:
        neighbors.append((x+1, y, 2, 8))
    if x > 0 and not visited[y][x-1]:
        neighbors.append((x-1, y, 8, 2))
    return neighbors

def carve_maze(grid, visited, start_pos, width, height):
    x, y = start_pos
    visited[y][x] = True
    stack = [(x, y)]

    while stack:
        curr_x, curr_y = stack[-1]
        neighbors = get_unvisited_neighbors(curr_x, curr_y, width, height, visited)

        if neighbors:
            nx, ny, wall_curr, wall_next = random.choice(neighbors)
            grid[curr_y][curr_x] -= wall_curr
            grid[ny][nx] -= wall_next
            visited[ny][nx] = True
            stack.append((nx, ny))
        else:
            stack.pop()

def make_imperfect(grid, width, height):
    """Knocks down random walls to create loops for an imperfect maze."""
    # Remove roughly 5% of the internal walls to create loops
    walls_to_remove = (width * height) // 20 
    
    removed = 0
    while removed < walls_to_remove:
        x = random.randint(1, width - 2)
        y = random.randint(1, height - 2)
        
        if grid[y][x] & 1:  
            grid[y][x] -= 1
            grid[y-1][x] -= 4
            removed += 1

def generate_maze(width, height, entry, exit, perfect):
    """A maze generator"""
    grid, visited = init_maze(width, height)
    apply_42_stamp(visited, width, height)
    if visited[entry[1]][entry[0]]: 
        raise ValueError("Entry coordinate is blocked by the 42 stamp.")
    carve_maze(grid, visited, entry, width, height)
    if not  perfect:
        make_imperfect(grid, width, height)
    return grid


def print_maze_solid(grid, width, height):
    """
    Renders the maze using solid ██ blocks for walls.
    """
    # 1. Print the top boundary (North walls of the first row)
    top_line = "██" * (width * 2 + 1)
    print(top_line)

    for y in range(height):
        # row_str starts with the West boundary wall
        row_str = "██" 
        # sub_str handles the South walls below the current row
        sub_str = "██"

        for x in range(width):
            val = grid[y][x]
            
            # The Cell Space (always empty/path)
            row_str += "  "
            
            # The East Wall (Bit 2)
            if val & 2:
                row_str += "██"
            else:
                row_str += "  "

            # The South Wall (Bit 4)
            if val & 4:
                sub_str += "██"
            else:
                sub_str += "  "
            
            # The Corner (Always solid to keep the grid connected)
            sub_str += "██"

        print(row_str)
        print(sub_str)

if __name__ == "__main__":
    W, H = 25, 11
    test_grid = generate_maze(W, H, (0, 0), (W-1, H-1), True)
    
    print(f"Generated {W}x{H} Maze:")
    print_maze_solid(test_grid, W, H)