class Solution:
    def myAtoi(self, s: str) -> int:
        negativeSign = False
        result = ""
        if not s:
            return 0
        while s:
            if s[0] == " ":
                s = s[1:]
            else:
                break
        if s:
            if s[0] == "+":
                s = s[1:]
            elif s[0] == "-":
                negativeSign = True
                s = s[1:]

        while s:
            if s[0].isdigit():
                result += s[0]
                s = s[1:]
            else:
                break

        if result == "":
            return 0
        result = int(result)

        if negativeSign:
            result = - result
            result = max(result, 0 - pow(2, 31))
        else:
            result = min(result, pow(2, 31) - 1)
        return result


if __name__ == "__main__":
    S = Solution()

    print(S.myAtoi("      +-12"))
