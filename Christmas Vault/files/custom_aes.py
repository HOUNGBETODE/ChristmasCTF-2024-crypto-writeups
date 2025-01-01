from typing import List
from sympy import Matrix
import numpy as np, pickle, random
from secret import Img2Matrix, message # custom module imported here


ALPHABET = "sby}!mvah8Gf_*6ktrW40C1jlu357wxdT2gpeo {zFi9cnMq="


class AESCBC:
    def __init__(self, key: np.ndarray):
        if key.shape not in ((16, 16), (24, 24), (32, 32)):
            raise ValueError("Key must be a squarred matrix of size 16, 24 or 32.")
        self.key = key
        self.n = key.shape[0]
        self.inv_key = Matrix(self.key).inv_mod(len(ALPHABET))


    def encrypt(self, plaintext: str) -> str:
        iv = ''.join(random.choices(ALPHABET, k=16))  # Generate a random IV (16 bytes)

        # Pad the plaintext to make it a multiple of the squarred matrix key size
        plaintext += ALPHABET[-1] * (len(plaintext) % self.n)
        output_blocks = [iv]

        # Encrypt the data
        ciphertext = ""
        for index in range(0, len(plaintext), self.n):
            ciphertext += self.black_box(self.black_xor(plaintext[index : index + self.n], output_blocks[-1]))
            output_blocks.append(ciphertext[-16:])

        # returning iv and ciphertext
        return iv, ciphertext


    def decrypt(self, iv: str, ciphertext: str) -> str:
        if len(iv) != 16:
            raise ValueError("IV must be 16 characters.")


    def text_to_numbers(self, data : str) -> List[int]:
        return [ALPHABET.index(char) for char in data]


    def numbers_to_text(self, numbers : List[int]) -> str:
        return ''.join(ALPHABET[num] for num in numbers)


    def black_xor(self, data_1 : str, data_2 : str) -> str:
        blacktext = ""
        for pt_char, key_char in zip(data_1, data_2):
            black_char = ALPHABET[(ALPHABET.index(pt_char) + ALPHABET.index(key_char)) % len(ALPHABET)]
            blacktext += black_char 
        return blacktext


    def black_box(self, data : str) -> str:
        whitetext_numbers = self.text_to_numbers(data)
        blocks = np.array(whitetext_numbers).reshape(-1, self.n)
        black_numbers = np.dot(blocks, self.key) % len(ALPHABET)
        return self.numbers_to_text(black_numbers.flatten())



if __name__ == "__main__":
    custom_key = Img2Matrix("self.key.png").load()
    cipher = AESCBC(key=custom_key)

    with open("output.bin", "wb") as file:
        pickle.dump(cipher.encrypt(message), file)

# N.B : Flag is concealed within variable [message].