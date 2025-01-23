def longest_sub_string_without_repeat(s):
    start = 0
    max_length = 0
    char_index_map = {}

    for char_position, char in enumerate(s):
        print(f"char_position: {char_position}, char: {char}")
        if char in char_index_map and char_index_map[char] >= start:
            print(f"char_index_map: {char_index_map}, char: {char}")
            start = char_index_map[char] + 1
            print(f"start: {start}")

        char_index_map[char] = char_position
        print(f"XXXX-char_index_map: {char_index_map}")
        max_length = max(max_length, char_position - start + 1)
        print(f"max_length: {max_length}")

    return max_length


if __name__ == '__main__':
    print(longest_sub_string_without_repeat('abcabcd'))
