def romanToInt(s: str) -> int:
    sum = 0
    i = (len(s)-1)
    while i >= 0:
        if s[i] == "I":
            sum += 1
            i -= 1
        if s[i] == "V":
            if i-1 >= 0 and s[i - 1] == "I":
                sum += 4
                i -= 2
            else:
                sum += 5
                i -= 1
        if s[i] == "X":
            if i-1 >= 0 and s[i - 1] == "I":
                sum += 9
                i -= 2
            else:
                sum += 10
                i -= 1
        if s[i] == "L":
            if i-1 >= 0 and s[i - 1] == "X":
                sum += 40
                i -= 2
            else:
                sum += 50
                i -= 1
        if s[i] == "C":
            if i-1 >= 0 and s[i - 1] == "X":
                sum += 90
                i -= 2
            else:
                sum += 100
                i -= 1
        if s[i] == "D":
            if i-1 >= 0 and s[i - 1] == "C":
                sum += 400
                i -= 2
            else:
                sum += 500
                i -= 1
        if s[i] == "M":
            if i-1 >= 0 and s[i - 1] == "C":
                sum += 900
                i -= 2
            else:
                sum += 1000
                i -= 1
    return sum


if __name__ == "__main__":
    print(romanToInt("MMMCDXC"))
