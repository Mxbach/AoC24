def one_star(pages: list[str], rules: dict):
    counter = 0
    for p in pages:
        correct = True
        nums = p.split(',')
        for n in nums:
            rule = rules.get(n)
            if rule:
                for r in rule:
                    if r in nums and nums.index(r) < nums.index(n):
                        correct = False
        if correct:
            counter += int(nums[len(nums)//2])
    return counter

def two_star(pages:list[str], rules: dict):
    counter = 0
    for p in pages:
        nums = p.split(',')

        correct = True
        change = True
        while change:
            change = False
            for i, n in enumerate(nums):
                rule = rules.get(n)
                if rule:
                    for r in rule:
                        if r in nums[:i]:
                            nums.remove(r)
                            nums.append(r)
                            change = True
                            if correct:
                                correct = False

        if not correct:
            counter += int(nums[len(nums)//2])

    return counter


def main():
    with open("../inputs/input5.txt", 'r') as f:
        rules_raw = f.readlines()

    pages = [i.strip() for i in rules_raw[rules_raw.index('\n')+1:]]
    rules_raw = [i.strip() for i in rules_raw[:rules_raw.index('\n')]]

    rules = {}
    for r in rules_raw:
        one_rule = r.split('|')
        k, v = one_rule[0], one_rule[1]
        if not rules.get(k):
            rules[k] = [v]
        else:
            rules.get(k).append(v)

    print(f"⭐: {one_star(pages, rules)}")
    print(f"⭐⭐: {two_star(pages, rules)}")


if __name__ == "__main__":
    main()
