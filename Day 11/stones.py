import sys
sys.set_int_max_str_digits(10000000)

def main():
    with open("../inputs/input11.txt", 'r') as f:
        input = f.readlines()

    l = [i for i in input[0].strip().split()]
    print(l)

    for it in range(25):
        print(f"Iteration {it}")
        for i, el in enumerate(l):
            cp = l[:]

            if el == 0:
                cp[i] = str(1)
            
            elif len(el) % 2 == 0:
                part1 = el[:len(el)//2]
                part2 = el[len(el)//2]

                cp[i] = part2
                cp.insert(i, part1)
            
            else:
                cp[i] = str(int(cp[i] * 2024))
            
            l = cp
        print(len(l))
    print(len(l))

if __name__ == "__main__":
    main()