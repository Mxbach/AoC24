import numpy as np
from enum import Enum



class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

moving_coords = {
    Direction.UP: (-1, 0),
    Direction.RIGHT: (0, 1),
    Direction.DOWN: (1, 0),
    Direction.LEFT: (0, -1)
}

guard = 69
obstacle = -1
visited = 1

def one_star(I, J, area, direction, x, y) -> int:
    while True:
        i, j = moving_coords[direction]
        nx, ny = x + i, y + j
        if 0 <= nx < I and 0 <= ny < J:
            if area[nx, ny] == obstacle:
                direction = Direction((direction.value + 1) % 4)

            else:
                area[x, y] = visited
                x, y = nx, ny
                area[x, y] = guard
        else:
            break

    return np.sum(area == visited)

def two_star(I, J, area, direction, x, y) -> int:
    start_x, start_y = x, y
    start_dir = direction.value
    start_area = np.copy(area)
    count = 0
    iteration = 0

    for i in range(I):
        for j in range(J):
            print(f"Iteration {iteration + 1} of {I * J}")
            iteration += 1

            if i == start_x and j == start_y:
                continue

            x, y = start_x, start_y
            direction = Direction(start_dir)

            original_value = area[i, j]
            area[i, j] = obstacle

            visited_states = set()

            while True:
                current_state = (x, y, direction)
                if current_state in visited_states:
                    print(f"Infinite loop detected at state {current_state}")
                    count += 1
                    break
                visited_states.add(current_state)

                dx, dy = moving_coords[direction]
                nx, ny = x + dx, y + dy

                if not (0 <= nx < I and 0 <= ny < J):
                    break

                if area[nx, ny] == obstacle:
                    direction = Direction((direction.value + 1) % 4)
                else:
                    area[x, y] = visited
                    x, y = nx, ny
                    area[x, y] = guard

            area[i, j] = original_value

    return count

from concurrent.futures import ProcessPoolExecutor

def worker(start_i, end_i, start_j, end_j, I, J, area, direction, x, y) -> int:
    start_x, start_y = x, y
    start_dir = direction.value
    start_area = np.copy(area)
    count = 0
    iteration = 0

    for i in range(start_i, end_i):
        for j in range(start_j, end_j):
            print(f"Iteration {iteration + 1} of {(end_i - start_i) * (end_j - start_j)}")
            iteration += 1

            if i == start_x and j == start_y:
                continue

            x, y = start_x, start_y
            direction = Direction(start_dir)

            original_value = area[i, j]
            area[i, j] = obstacle

            visited_states = set()

            while True:
                current_state = (x, y, direction)
                if current_state in visited_states:
                    print(f"Infinite loop detected at state {current_state}")
                    count += 1
                    break
                visited_states.add(current_state)

                dx, dy = moving_coords[direction]
                nx, ny = x + dx, y + dy

                if not (0 <= nx < I and 0 <= ny < J):
                    break

                if area[nx, ny] == obstacle:
                    direction = Direction((direction.value + 1) % 4)
                else:
                    area[x, y] = visited
                    x, y = nx, ny
                    area[x, y] = guard

            area[i, j] = original_value

    return count

def two_star_parallel() -> int:
    pass
    
def main():
    with open("../inputs/input6.txt", 'r') as f:
        raw_data = f.readlines()

    I, J = len(raw_data), len(raw_data[0].strip())
    area = np.zeros((I, J), dtype=np.int8)

    direction: Direction = Direction.UP
    x, y = -1 , -1
    for i in range(I):
        for j in range(J):
            value = 0
            if raw_data[i][j] == '#':
                value = obstacle
            elif raw_data[i][j] == '^':
                value = guard
                x, y = i, j
            
            area[i, j] = value
    
    

    print("⭐:", one_star(I, J, area, direction, x, y))
    print("⭐⭐:", two_star(I, J, area, direction, x, y))
                

if __name__ == "__main__":
    main()