def romanToInt(s: str) -> int:
    SYMBOLS = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    solution = 0

    for sym in range(0, len(s) - 1):
        if SYMBOLS[s[sym]] < SYMBOLS[s[sym + 1]]:
            solution -= SYMBOLS[s[sym]]
        else:
            solution += SYMBOLS[s[sym]]

    solution += SYMBOLS[s[-1]]
    return solution


if __name__ == "__main__":
    print(romanToInt("III"))
