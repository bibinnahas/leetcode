def is_subsequence(comparing_string: str, main_string: str) -> bool:
    comparing_string_index, main_string_index = 0, 0
    while comparing_string_index < len(comparing_string) and main_string_index < len(main_string):
        if comparing_string[comparing_string_index] == main_string[main_string_index]:
            comparing_string_index += 1
        main_string_index += 1
    return comparing_string_index == len(comparing_string)


if __name__ == '__main__':
    print(is_subsequence("abc", "deahgdc"))
