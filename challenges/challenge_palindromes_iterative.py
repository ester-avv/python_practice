def is_palindrome_iterative(word: str):
    size = len(word)
    if size == 0:
        return False

    # no loop compara o elem no index i com a posição contraria
    # se for igual e palind
    for i in range(size // 2):
        if word[i] != word[size - 1 - i]:
            return False
    return True
    """ raise NotImplementedError """
