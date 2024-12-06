def valid_list(l: list[int]) -> bool:
    if not (l == list(sorted(l, reverse=True)) or l == list(sorted(l))):
        return False
    
    dist = True
    for i in range(1, len(l)):
        if not (1 <= abs(l[i-1] - l[i]) <= 3):
            dist = False

    return dist

def one_star(l: list[list[int]]) -> int:
    valid = 0
    for i in l:
        if valid_list(i):
            valid += 1
    return valid

def two_star(l: list[list[int]]):
    valid = 0
    for i in l:
        if valid_list(i):
            valid += 1
        else:
            res = []
            for j in range(len(i)):
                cp = i.copy()
                cp.pop(j)
                res.append(valid_list(cp))
            
            if True in res:
                valid += 1
    return valid

def main():
    with open("./input.txt", 'r') as f:
        raw = f.readlines()

    l = []
    for r in raw:
        l.append([int(x) for x in r.strip().split()])

    print(one_star(l))
    print(two_star(l))

if __name__ == "__main__":
    main()