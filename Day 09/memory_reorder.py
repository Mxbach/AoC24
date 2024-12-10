from itertools import chain

def two_star(input: str) -> int:
    memory: list[tuple[int, int]] = []
    id = 0
    for i in range(len(input)):
        num = int(input[i])
        if i % 2 == 0:
            memory.append((num, id))
            id += 1
        else:
            memory.append((num, -1))
    
    back_it = len(memory) - 1

    while 0 < back_it:
        cp = memory[:]
        while 0 < back_it and memory[back_it][1] == -1:
            back_it -= 1

        # print(back_it)
        need, id = memory[back_it]

        for i in range(back_it):
            sp, mem = memory[i]
            
            if sp >= need and mem == -1:
                cp[i] = (need, id)
                cp[back_it] = (need, -1)
                if sp > need:
                    cp.insert(i+1, (sp - need, -1))
                break
    
        memory = cp[:]
        back_it -= 1
    final_memory = list(chain.from_iterable([[id] * space for space, id in memory]))

    return sum(i * el for i, el in enumerate(final_memory) if el != -1)

def one_star(input: str) -> int:
    memory = []
    id = 0
    for i in range(len(input)):
        num = int(input[i])
        if i % 2 == 0:
            memory.extend([id] * num)
            id += 1
        else:
            memory.extend([-1] * num)


    back_it = len(memory) - 1
    it = 0

    while it < back_it:
        while it < back_it and memory[it] != -1:
            it += 1
        while it < back_it and memory[back_it] == -1:
            back_it -= 1

        if it < back_it and memory[it] == -1:
            memory[it] = memory[back_it]
            memory[back_it] = -1

    return sum(i * el for i, el in enumerate(memory) if el != -1)

def main():
    with open("../inputs/input9.txt", 'r') as f:
        input = [i.strip() for i in f.readlines()][0]

    print("⭐:", one_star(input))
    print("⭐⭐:", two_star(input))
    # print("⭐⭐:", two_star("2333133121414131402"))

if __name__ == "__main__":
    main()