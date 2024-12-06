import numpy as np

options = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Top-left
    (-1, 1),  # Top-right
    (1, -1),  # Bottom-left
    (1, 1)    # Bottom-right
]

def one_star(s: str, field: np.ndarray[np.ndarray], x: int, y: int, direction: tuple[int, int]):
    if s == "XMAS":
        return 1
    if len(s) >= 4:
        return 0
    
    i, j = direction
    idx, idy = x + i, y + j
    
    if 0 <= idx < field.shape[0] and 0 <= idy < field.shape[1]:
        return one_star(s + field[idx, idy], field, idx, idy, direction)
    
    return 0

def two_star(field: np.ndarray[np.ndarray]):
    occurences = 0
    for i in range(1, field.shape[0] - 1):
        for j in range(1, field.shape[1] - 1):
            if field[i, j] == "A":
                X = ""
                for x, y in options[4:]:
                    idx, idy = i + x, j + y
                    if 0 <= idx < field.shape[0] and 0 <= idy < field.shape[1]:
                        X += field[idx, idy]

                if X.count("M") == 2 and X.count("S") == 2 and X != "MSSM" and X != "SMMS":
                    occurences += 1

    return occurences

    
def main():
    with open("./input.txt", 'r') as f:
        field = np.array([[j for j in i.strip()] for i in f.readlines()])

    one = 0
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i, j] != "X":
                continue
            
            for o in options:
                one += one_star("X", field, i, j, o)
    
    print(f"⭐: {one}")
    print(f"⭐⭐: {two_star(field)}")


if __name__ == "__main__":
    main()