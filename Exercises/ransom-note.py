def canConstruct(ransomNote: str, magazine: str) -> bool:
    dictionary = {}
    for letter in magazine:
        if dictionary.get(letter) is not None:
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1

    for letter in ransomNote:
        if dictionary.get(letter) is not None and dictionary.get(letter) > 0:
            dictionary[letter] -= 1
        else:
            return False
    return True


if __name__ == "__main__":
    print(canConstruct("aaa", "magazine"))
