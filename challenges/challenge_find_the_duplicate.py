def find_duplicate(nums):
    check_array(nums)
    dup_numbers = set()
    """o set cria um dicionario ordenado"""
    """Returns : An empty set if no element is passed.
    --> Non-repeating element iterable modified as passed as argument"""
    if not check_number(nums):
        return False
    for number in nums:
        if number in dup_numbers:
            return number
        else:
            dup_numbers.add(number)
    return False


def check_array(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False


def check_number(nums):
    try:
        for num in nums:
            if num < 0 or type(num) != int:
                return False
        return True
    except TypeError:
        return False


""" raise NotImplementedError """
