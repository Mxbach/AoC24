def one_two_star(stones, iterations):
    d = {i: 1 for i in stones}
    
    for _ in range(iterations):
        
        new_dict = {}
        for key, value in d.items():
            if key == 0:
                if not new_dict.get(1):
                    new_dict[1] = value
                else:
                    new_dict[1] += value
            
            elif len(str(key)) % 2 == 0:
                mid = len(str(key)) // 2
                part1 = int(str(key)[:mid])
                part2 = int(str(key)[mid:])

                if not new_dict.get(part1):
                    new_dict[part1] = value
                else:
                    new_dict[part1] += value

                if not new_dict.get(part2):
                    new_dict[part2] = value
                else:
                    new_dict[part2] += value

            else:
                new_val = key * 2024
                if not new_dict.get(new_val):
                    new_dict[new_val] = value
                else:
                    new_dict[new_val] += value
        
        d = new_dict
    
    return sum(value for _, value in d.items())

def main():
    with open("../inputs/input11.txt", 'r') as f:
        input = f.readlines()

    l = [int(i) for i in input[0].strip().split()]

    
    print("⭐:", one_two_star(l, 25))
    print("⭐⭐", one_two_star(l, 75))


if __name__ == "__main__":
    main()