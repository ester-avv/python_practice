def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    # initialize the dictionary
    counts = {}

    # loop simultaneously through the characters of the two strings.
    for c1, c2 in zip(first_string, second_string):
        if c1 in counts.keys():
            counts[c1] += 1
        else:
            counts[c1] = 1
        if c2 in counts.keys():
            counts[c2] -= 1
        else:
            counts[c2] = -1

    # Loop through the dictionary values.
    # if the dictionary contains even one value which is
    # different than 0, the strings are not anagrams.
    for count in counts.values():
        if count != 0:
            return False
    return True
