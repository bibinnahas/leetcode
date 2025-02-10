def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    char_to_word = {}
    word_to_char = {}

    if len(words) != len(pattern):
        return False

    for char, word in zip(pattern, words):
        print(char_to_word, word_to_char)
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            if word in word_to_char:
                return False
        char_to_word[char] = word
        word_to_char[word] = char

    return True


if __name__ == '__main__':
    print(word_pattern("abba", "dog cat cat dog"))  # Output: True
