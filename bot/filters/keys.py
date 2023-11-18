class CheckKey:
    """Filter to validate user entered key"""
    @staticmethod
    def caesar(key: str) -> bool:
        try:
            return int(key) > 0 and int(key) <= 10000
        except:
            return False

    @staticmethod
    def vigenere(key: str) -> bool:
        return key.isalpha()

    @staticmethod
    def atbash(key: str) -> bool:
        return key.isalpha()

    @staticmethod
    def aes(key: str) -> bool:
        return True
