def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        first = array[0]
        the_minor = [x for x in array[1:] if x < first]
        # pra cada x no array se for menor q o primeiro vai pro primeiro
        the_greater = [x for x in array[1:] if x >= first]
        return quicksort(the_minor) + [first] + quicksort(the_greater)


def is_anagram(first_string, second_string):
    lower_first_str = first_string.lower()
    lower_sec_str = second_string.lower()

    new_firs_str = "".join(quicksort(lower_first_str))
    new_sec_str = "".join(quicksort(lower_sec_str))

    if len(new_firs_str) == 0 or len(new_sec_str) == 0:
        return (new_firs_str, new_sec_str, False)
    if new_firs_str == new_sec_str:
        return (new_firs_str, new_sec_str, True)
    else:
        return (new_firs_str, new_sec_str, False)
