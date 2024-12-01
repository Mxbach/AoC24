def one_star(l, r) -> int:
    sum = 0
    for i, j in zip(l, r):
        sum += abs(i - j)
    
    return sum

def two_star(l, r) -> int:
    sum = 0
    for i in l:
        sum += i * r.count(i)
    
    return sum

def main():
    with open("./input.txt", 'r') as f:
        raw = f.readlines()
    
    l, r = [], []
    for i in raw:
        pair = i.strip().split()
        l.append(int(pair[0]))
        r.append(int(pair[1]))

    l = list(sorted(l))
    r = list(sorted(r))

    print(one_star(l, r))
    print(two_star(l, r))
    
if __name__ == "__main__":
    main()