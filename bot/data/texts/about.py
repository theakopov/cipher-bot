description_ciphers = {
    "caesar": """<b>Caesar cipher</b>
    
The Caesar cipher is a basic encryption method that involves shifting the letters of the alphabet by a fixed number of positions.
It was named after Julius Caesar, who is believed to have used it for military communications.
Each letter in the plaintext is replaced by a letter that is a fixed number of positions ahead in the alphabet.
For example, when offset by 3, "A" becomes "D", "B" becomes "E", and so on. The same shift is used for decryption.

The Caesar cipher is considered weak and can be easily deciphered. It is mainly used for educational purposes and as a basis for more advanced encryption methods.

The following languages are supported: Russian, English, Spanish

Crypto resistance 3/10""",

    "vigenere": """<b>Vigenere cipher</b>

The Vigenère cipher is a more advanced form of the polyalphabetic substitution cipher, named after the French cryptographer Blaise de Vigenère.
Unlike the Caesar cipher, which uses a fixed shift for each letter, the Vigenère cipher uses a keyword to determine the shift pattern.
The keyword is repeated to match the length of the plaintext, and each letter in the keyword determines the shift amount for the corresponding letter in the plaintext.

The Vigenère cipher provides a stronger encryption than the Caesar cipher. It was considered invulnerable for several centuries, until advances in cryptanalysis revealed its vulnerabilities.

The following languages are supported: Russian, Englisha, Spanish.

Crypto resistance 5/10""",

    "atbash": """<b>Atbash cipher</b>

The Atbash cipher is a substitution cipher that works by reversing the alphabet. This is one of the simplest encryption methods.
In the Atbash cipher, each letter in the plaintext is replaced by the corresponding letter from the opposite end of the alphabet.
For example, "A" is replaced by "Z", "B" by "Y" and so on. The same substitution is used for decryption.

The Atbash cipher provides an easy way to hide the meaning of a message, but provides minimal security and can be easily decrypted.
It is mainly used for educational purposes and as a historical example of a substitution cipher.

Crypto resistance 1/10""",

    "aes": """<b>AES cipher</b>

Advanced Encryption Standard (AES) - a symmetric block cipher.
It has been selected by the US National Institute of Standards and Technology (NIST) as a replacement for the Data Encryption Standard (DES).
AES works with data blocks of a fixed size and supports 128-, 192-, and 256-bit keys.
It uses multiple rounds of substitution, permutation, and XOR operations to provide a high level of security.

Crypto resistance 9/10"""
}
