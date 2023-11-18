import pytest
import string

from bot.misc.ciphers import Cipher

# The correctness of the key
# is checked in bot/filters/keys.py

caesar: list[tuple[str | int]] = [
    ("Это test datos | ё ñ", 34, "encrypt", "Юуп alza khavz | ж u"),
    ("Юуп alza khavz | ж u", 34,
     "decrypt", "Это test datos | ё ñ"),
    (string.punctuation, 10000,
     "encrypt", string.punctuation)
]

vigenere: list[tuple[str | int]] = [
    ("Это test datos | ё ñ", "_Шифр!=Хэш_ёñ",
     "encrypt", "Хыг kzvr jñrxn | ц j"),
    ("ab", "abcd", "encrypt", "ac"),
    ("abcd", "b", "encrypt", "bcde"),
]

atbash: list[tuple[str | int]] = [
    ("c", "abCdefghijklmnopqrstuvwxyz", "x"),
    ("y", "x", "y"),
    ("ab", "ab", "ba"),
    ("ax", "a", "ax"),
    ("c", "abcde", "c")
]

aes: list[tuple[str | int]] = [
    ("Something", "Something", "decrypt"),
    ("Text", "Key", "encrypt"),
    ("äåé∛®áßðö≷ ℸ⠉⡉㉈⭑🄸ⵓঊఃོႳ໒Լᢕ⫚㈥𝋡㊽𐇳☜ᶉ🕱℃🖵⑂ↂ", "äåé∛®áßðö≷ ℸ⠉⡉㉈⭑🄸ⵓঊఃོႳ໒Լᢕ⫚㈥𝋡㊽𐇳☜ᶉ🕱℃🖵⑂ↂ", "encrypt"),
]


def invertor(action: str) -> str:
    return "encrypt" if action == "decrypt" else "decrypt"


@pytest.mark.parametrize("text, key, action, correct", caesar)
def test_caesar(text: str, key: int, action: str, correct: str):
    assert Cipher.caesar(text, key, action) == correct

    # Compatibility check
    result = Cipher.caesar(
        Cipher.caesar(text, key, action),
        key,
        invertor(action))
    assert result == text


@pytest.mark.parametrize("text, key, action, correct", vigenere)
def test_vigenere(text: str, key: int, action: str, correct: str):
    assert Cipher.vigenere(text, key, action) == correct

    # Compatibility check
    result = Cipher.vigenere(
        Cipher.vigenere(text, key, action),
        key,
        invertor(action))
    assert result == text


@pytest.mark.parametrize("text, key, correct", atbash)
def test_atbash(text: str, key: int, correct: str):
    assert Cipher.atbash(text, key) == correct

    # Compatibility check
    result = Cipher.atbash(
        Cipher.atbash(text, key),
        key)
    assert result == text


@pytest.mark.parametrize("text, key, action", aes)
def test_aes(text: str, key: int, action: str):
    if action == "decrypt":
        assert Cipher.aes(text, key, action) == "---Failed to decrypt---"
        return

    # Compatibility check
    result = Cipher.aes(
        Cipher.aes(text, key, action),
        key,
        invertor(action))
    assert result == text
