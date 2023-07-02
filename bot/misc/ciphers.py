import hashlib
import base64

from Crypto.Cipher import AES
from Crypto import Random
from typing import Optional

from ..data.data import *


class Cipher:
    """
    Class for implementing ciphers
    """
    CIPHERS = {
        "Caesar cipher": "caesar",
        "Vigenere cipher": "vigenere",
        "Atbash cipher": "atbash",
        "AES": "aes",
    }

    @staticmethod
    def caesar(text: str, key: Optional[int], action: Optional[str] = None) -> str:
        """"
        Implementation of the Caesar cipher

        :param text: text to be encrypted/decrypted
        :param key: encryption/decryption key
        :param action: Indicates what needs to be done. Can be either encrypt or decrypt
        """
        try:
            key = int(key)
        except TypeError:
            raise TypeError("Key in caesar cipher must be integer")
        r = ""
        if action != "encrypt":
            key = key * -1
        for letter in text:
            if letter not in all:
                r += letter
                continue

            elif letter in en:
                new_letter = en[(en.index(letter) + key) % 26]
            elif letter in en_:
                new_letter = en_[(en_.index(letter) + key) % 26]
            elif letter in ru:
                new_letter = ru[(ru.index(letter) + key) % 33]
            elif letter in ru_:
                new_letter = ru_[(ru_.index(letter) + key) % 33]
            elif letter in es:
                new_letter = es[(es.index(letter) + key) % 27]
            elif letter in es_:
                new_letter = es_[(es_.index(letter) + key) % 27]
            r += new_letter
        return r

    @staticmethod
    def vigenere(text: str, key=str, action: Optional[str] = None) -> str:
        """"
        Implementation of the Vigenere cipher

        :param text: text to be encrypted/decrypted
        :param key: encryption/decryption key
        :param action: Indicates what needs to be done. Can be either encrypt or decrypt
        """
        r = ""
        len_key = len(key)
        iter = 0
        is_decrypt = 1
        if action != "encrypt":
            is_decrypt = -1

        for letter in text:
            if letter not in all:
                r += letter
                continue

            # shift definition
            while key[iter] not in all:
                iter += 1
            new_key = key[iter]
            if new_key.lower() in en:
                shift = en.index(new_key.lower())
            elif new_key.lower() in ru:
                shift = ru.index(new_key.lower())
            shift *= is_decrypt

            if letter in en_:
                index = en_.index(letter)
                new_letter = en_[(shift + index) % 26]
            elif letter in en:
                index = en.index(letter)
                new_letter = en[(shift + index) % 26]
            elif letter in ru_:
                index = ru_.index(letter)
                new_letter = ru_[(shift + index) % 33]
            elif letter in ru:
                index = ru.index(letter)
                new_letter = ru[(shift + index) % 33]
            r += new_letter

            iter += 1
            if iter >= len_key:
                iter = 0
        return r

    @staticmethod
    def atbash(text: str, alphabet: str, action: Optional[str] = None) -> str:
        """"
        Implementation of the Atbash cipher

        :param text: text to be encrypted/decrypted
        :param key: encryption/decryption key
        :param action: Indicates what needs to be done. Can be either encrypt or decrypt
        """
        r = ""
        new_alphabet = list(reversed(alphabet))
        for letter in text:

            if letter.lower() in alphabet:
                r += new_alphabet[alphabet.index(letter.lower())]
            else:
                r += letter
        return r

    @staticmethod
    def aes(text: str, key: str, action: Optional[str] = None) -> str:
        """"
        Implementation of the AES cipher

        :param text: text to be encrypted/decrypted
        :param key: encryption/decryption key
        :param action: Indicates what needs to be done. Can be either encrypt or decrypt
        """
        def _pad(text):
            return text + (bs - len(text.encode()) % bs) * chr(bs - len(text.encode()) % bs)

        def _unpad(text):
            return text[:-ord(text[len(text)-1:])]

        bs = AES.block_size
        key = hashlib.sha256(key.encode()).digest()

        if action == "encrypt":
            text = _pad(text)
            iv = Random.new().read(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            result = base64.b64encode(
                iv + cipher.encrypt(text.encode())).decode()

        else:
            try:
                text = base64.b64decode(text)
                iv = text[:AES.block_size]
                cipher = AES.new(key, AES.MODE_CBC, iv)
                result = _unpad(cipher.decrypt(
                    text[AES.block_size:])).decode('utf-8')
            except Exception:
                result = "---Failed to decrypt---"
        return result
