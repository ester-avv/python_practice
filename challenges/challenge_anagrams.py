# algoritimo merge pertence a Trybe
def merge_sort(numbers, start=0, end=None):
    end = end or len(numbers)
    if end is None:
        end = len(numbers)
    if (end - start) > 1:  # se não reduzi o suficiente, continua
        mid = (start + end) // 2  # encontrando o meio
        merge_sort(numbers, start, mid)  # dividindo as listas
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)  # unindo as listas


# função auxiliar que realiza a mistura dos dois arrays


def merge(numbers, start, mid, end):
    left = numbers[start:mid]  # indexando a lista da esquerda
    right = numbers[mid:end]  # indexando a lista da direita

    left_index, right_index = 0, 0  # as duas listas começarão do início

    for general_index in range(start, end):  # percorrer sobre a lista inteira
        if (
            left[left_index] < right[right_index]
        ):  # se o elemento do topo da esquerda for menor que o da direita,
            # ele será o escolhido
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
            # se os elementos da esquerda acabaram, preenche o restante com
            # a lista da direita

        elif right_index >= len(
            right
        ):  # se os elementos da direita acabaram, preenche o restante com
            # a lista da esquerda
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[
                right_index
            ]  # caso o da direita seja menor, ele será o escolhido
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    firs_str = list(first_string.lower())
    sec_str = list(second_string.lower())
    merge_sort(firs_str)
    merge_sort(sec_str)

    first_string = "".join(firs_str)
    second_string = "".join(sec_str)

    if not first_string or not second_string:
        return first_string, second_string, False
    if first_string == second_string:
        return first_string, second_string, True

    return first_string, second_string, False
