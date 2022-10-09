def are_anagram(s1: str, s2: str) -> bool:
    """
    Simple function which will return True if two strings are anagram of each other
    """
    s1 = standardise_string(s1)
    s2 = standardise_string(s2)

    return sorted(s1) == sorted(s2)


def are_anagram_no_sort(s1: str, s2: str) -> bool:
    """
    Function which will return True if 2 strings are anagrams,
    withour using Python sorted() function
    """
    s1 = standardise_string(s1)
    s2 = standardise_string(s2)

    char_tracker = {}

    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in char_tracker:
            char_tracker[char] += 1
        else:
            char_tracker[char] = 1

    for char in s2:
        if char in char_tracker:
            char_tracker[char] -= 1
        else:
            char_tracker[char] = 1

    for char in char_tracker:
        if char_tracker[char] != 0:
            return False

    return True


def standardise_string(s: str) -> str:
    """
    simple function to standardise strings
    """
    return s.replace(' ', '').lower()
