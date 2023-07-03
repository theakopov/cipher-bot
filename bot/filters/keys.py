from typing import Optional


class CheckKey:
    """Filter to validate user entered key"""
    @staticmethod
    def caesar(key: Optional[str]) -> bool:
        try:
            return int(key) > 0 and int(key) <= 10000
        except:
            return False

    @staticmethod
    def vigenere(key: Optional[str]) -> bool:
        try:
            int(key)
            return False
        except ValueError:
            return True

    @staticmethod
    def atbash(key: Optional[str]) -> bool:
        return key.isalpha()

    @staticmethod
    def aes(key: Optional[str]) -> bool:
        return True
