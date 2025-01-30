def can_construct(ransom_note, magazine):
    char_count = {}
    for char in magazine:
        char_count[char] = char_count.get(char, 0) + 1

    for char in ransom_note:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1

    return True


if __name__ == '__main__':
    print(can_construct("aaa", "aabc"))
