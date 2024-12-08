import numpy as np
from itertools import combinations
from math import sqrt

def two_star(area: np.ndarray) -> int:
    counter = 0
    antinodes = set()
    for letter in np.unique(area):
        if letter == '.':
            continue

        positions = np.where(area == letter)
        coordinates = list(zip(positions[0], positions[1]))
        if len(coordinates) < 2:
            continue

        point_pairs = combinations(coordinates, 2)
        for (x1, y1), (x2, y2) in point_pairs:
            P = (x1, y1)
            T = (x2, y2)

            del_x = T[0] - P[0]
            del_y = T[1] - P[1]

            distance = sqrt((del_x)**2 + (del_y)**2)

            vec1 = np.array([del_x, del_y], dtype=np.float64)
            vec1_norm = vec1 / distance

            diagonal = np.round(sqrt((area.shape[0])**2 + (area.shape[1])**2)).astype(int)

            if not P in antinodes:
                counter += 1
                antinodes.add(P)
            for i in range(1, diagonal):
                vec1_scaled = vec1_norm * i * distance

                an1 = tuple(np.round(P + vec1_scaled).astype(int))
                an2 = tuple(np.round(T - vec1_scaled).astype(int))

                if 0 <= an1[0] < area.shape[0] and 0 <= an1[1] < area.shape[1] and not an1 in antinodes:
                    antinodes.add(an1)
                    counter += 1

                if 0 <= an2[0] < area.shape[0] and 0 <= an2[1] < area.shape[1] and not an2 in antinodes:
                    antinodes.add(an2)
                    counter += 1

    return counter

def one_star(area: np.ndarray):

    counter = 0
    antinodes = set()
    for letter in np.unique(area):
        if letter == '.':
            continue

        positions = np.where(area == letter)
        coordinates = list(zip(positions[0], positions[1]))
        if len(coordinates) < 2:
            continue

        point_pairs = combinations(coordinates, 2)
        for (x1, y1), (x2, y2) in point_pairs:
            P = (x1, y1) # np.array([x1, y1], dtype=np.float64)
            T = (x2, y2) # np.array([x2, y2], dtype=np.float64)

            del_x = T[0] - P[0]
            del_y = T[1] - P[1]

            distance = sqrt((del_x)**2 + (del_y)**2)

            vec1 = np.array([del_x, del_y], dtype=np.float64)
            vec1_norm = vec1 / distance
            vec1_scaled = vec1_norm * 2 * distance

            an1 = tuple(np.round(P + vec1_scaled).astype(int))
            an2 = tuple(np.round(T - vec1_scaled).astype(int))

            if 0 <= an1[0] < area.shape[0] and 0 <= an1[1] < area.shape[1] and not an1 in antinodes:
                antinodes.add(an1)
                counter += 1
            if 0 <= an2[0] < area.shape[0] and 0 <= an2[1] < area.shape[1] and not an2 in antinodes:
                antinodes.add(an2)
                counter += 1

    return counter

def main():
    with open("../inputs/input8.txt", 'r') as f:
        input = f.readlines()

    area = np.array([[j for j in i.strip()] for i in input], dtype=np.str_)

    print("⭐:", one_star(area))
    print("⭐⭐:", two_star(area))

if __name__ == "__main__":
    main()