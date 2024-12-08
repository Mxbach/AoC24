def rec_two_star(target: int, curr: int, numbers: list[int]) -> bool:
    if not numbers:
        return target == curr
        
    val = numbers[0]
    new_numbers = numbers[1:]

    return rec_two_star(target, curr + val, new_numbers) or rec_two_star(target, curr * val, new_numbers) or rec_two_star(target, int(str(curr) + str(val)), new_numbers)

def rec_one_star(target: int, curr: int, numbers: list[int]) -> bool:
    if not numbers:
        return target == curr
        
    val = numbers[0]
    new_numbers = numbers[1:]

    return rec_one_star(target, curr + val, new_numbers) or rec_one_star(target, curr * val, new_numbers)

def main():
    with open("../inputs/input7.txt", 'r') as f:
        input = f.readlines()

    one_star = 0
    two_star = 0
    for i in input:
        split = i.strip().split(": ")
        result, numbers = int(split[0]), [int(x) for x in split[1].split(" ")]

        if rec_one_star(result, 0, numbers):
            one_star += result
        
        if rec_two_star(result, 0, numbers):
            two_star += result

    print("⭐:", one_star)
    print("⭐⭐:", two_star)

if __name__ == "__main__":
    main()