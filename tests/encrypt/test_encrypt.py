# from challenges.challenge_encrypt_message import encrypt_message
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    pass
    text = 'abobora'
    all_reversed_text = 'aroboba'
    three_reversed_text = 'oba_arob'
    two_reversed_text = 'arobo_ba'

    assert encrypt_message("", 2) == ""
    assert encrypt_message(text, 0) == all_reversed_text
    assert encrypt_message(text, 10) == all_reversed_text
    assert encrypt_message(text, -10) == all_reversed_text
    assert encrypt_message(text, 7) == all_reversed_text
    assert encrypt_message(text, 3) == three_reversed_text
    assert encrypt_message(text, 2) == two_reversed_text
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message(text, "a")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 10)
