import re

def main():
    with open("input.txt", 'r') as f:
        s = f.read()

    matches = re.findall( r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", s)

    one_star = 0
    two_star = 0
    mode = True
    for m in matches:
        if 'do()' in m:
            mode = True
        
        elif "don't()" in m:
            mode = False

        else:
            x, y = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", m)[0]
            
            one_star += int(x) * int(y)

            if mode:
                two_star += int(x) * int(y)

    print(one_star)
    print(two_star)

if __name__ == "__main__":
    main()