import math

mapval = {
    "add": -1,
    "sub": -2,
    "mul": -3,
    "rem": -4,
    "pow": -5,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def values():
    global mapval
    mapval = {
        "add": -1,
        "sub": -2,
        "mul": -3,
        "rem": -4,
        "pow": -5,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }


def generate_value(s, stack):
    s += 'c'
    str_val = ""
    sn = ""
    for char in s:
        if char == 'c':
            if str_val not in mapval:
                return False
            sn += str(mapval[str_val])
            str_val = ""
        else:
            str_val += char

    ans = int(sn)
    stack.append(ans)
    return True


def solve_this(stack1, stack2):
    while stack1:
        top = stack1.pop()
        if top < 0 and len(stack2) < 2:
            return "expression is not complete or invalid"
        elif top < 0:
            val1 = stack2.pop()
            val2 = stack2.pop()
            if top == -1:
                new_val = val1 + val2
            elif top == -4:
                new_val = val1 % val2
            elif top == -2:
                new_val = val1 - val2
            elif top == -3:
                new_val = val1 * val2
            elif top == -5:
                new_val = int(math.pow(val1, val2))
            stack2.append(new_val)
        else:
            stack2.append(top)

    return str(stack2[0]) if len(stack2) == 1 else "expression is not complete or invalid"


def perform_task(s, stack):
    str_val = ""
    s += " "
    count_of_c = 0
    for i in range(len(s)):
        if s[i] == ' ':
            if str_val not in mapval:
                if count_of_c == 0:
                    return "expression evaluation stopped invalid words present"
                if not generate_value(str_val, stack):
                    return "expression evaluation stopped invalid words present"
                count_of_c = 0
            else:
                stack.append(mapval[str_val])
            str_val = ""
        else:
            if s[i] == 'c':
                count_of_c += 1
            str_val += s[i]
    return ""


def solve_it(s):
    st = []
    st1 = []
    an = perform_task(s, st)
    return an if an != "" else solve_this(st, st1)


def main():
    values()
    s = input()
    print(solve_it(s))


if __name__ == "__main__":
    main()

