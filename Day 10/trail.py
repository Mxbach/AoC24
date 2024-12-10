import numpy as np

options = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
]

def rec_two_star(t_map: np.ndarray, x: int, y: int) -> int:
    if t_map[x, y] == 9:
        return 1
    coords = [(x+dx, y+dy) for dx, dy in options]
    return sum(rec_two_star(t_map, nx, ny) for nx, ny in coords if 0 <= nx < t_map.shape[0] and 0 <= ny < t_map.shape[1] and t_map[x, y] + 1 == t_map[nx, ny])

def rec_one_star(t_map: np.ndarray, reached: set, x: int, y: int) -> int:
    if t_map[x, y] == 9 and not (x, y) in reached:
        reached.add((x, y))
        return 1
    coords = [(x+dx, y+dy) for dx, dy in options]
    return sum(rec_one_star(t_map, reached, nx, ny) for nx, ny in coords if 0 <= nx < t_map.shape[0] and 0 <= ny < t_map.shape[1] and t_map[x, y] + 1 == t_map[nx, ny])

def main():
    with open("../inputs/intput10.txt", 'r') as f:
        input = f.readlines()

    t_map = np.array([[int(l) for l in line.strip()]for line in input])

    X, Y = t_map.shape
    print("⭐:", sum(rec_one_star(t_map, set(), x, y) for x in range(X) for y in range(Y) if t_map[x, y] == 0))
    print("⭐⭐:", sum(rec_two_star(t_map, x, y) for x in range(X) for y in range(Y) if t_map[x, y] == 0))

if __name__ == "__main__":
    main()