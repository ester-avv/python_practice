def encrypt_message(message: str, key: int):
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    if key not in range(1, len(message)):
        return "".join(reversed(message))

    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)


""" Recebe uma string message e um inteiro key como parâmetros
Se key e message não possuírem os tipos corretos, uma exceção deve ser lançada
Se key não for um índice positivo válido de message,
retorna a string message invertida
Se key for ímpar:
divide message no índice key, inverte os caracteres de cada parte, e retorna
a união das partes novamente com "_" entre elas
Se key for par:
divide message no índice key, inverte a posição das partes, inverte os
caracteres de cada parte, e retorna a união das partes com "_" entre elas """
