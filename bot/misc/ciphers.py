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
            for alphabet in alphabets:
                if letter in alphabet:
                    new_letter = alphabet[(alphabet.index(
                        letter) + key) % len(alphabet)]

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
            for alphabet in alphabets:
                if new_key.lower() in alphabet:
                    shift = alphabet.index(new_key.lower())

            shift *= is_decrypt
            for alphabet in alphabets:
                if letter in alphabet:
                    new_letter = alphabet[(
                        alphabet.index(letter) + shift) % len(alphabet)]

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
