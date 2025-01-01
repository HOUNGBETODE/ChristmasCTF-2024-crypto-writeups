from typing import List
from sympy import Matrix
import numpy as np, pickle

# we re-write AESCBC class by adding some functional logics : decrypt(), black_xor_dec() and black_box_dec()
# taking a look at [AESCBC.png] inspires a lot about how to reverse the process and write a suitable decrypt() function

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

        # Pad the plaintext to make it a multiple of the block size (16 bytes for AES)
        plaintext += ALPHABET[-1] * (len(plaintext) % self.n)
        output_blocks = [iv]

        # Encrypt the data
        ciphertext = ""
        for index in range(0, len(plaintext), self.n):
            ciphertext += self.black_box_enc(self.black_xor_enc(plaintext[index : index + self.n], output_blocks[-1]))
            output_blocks.append(ciphertext[-16:])
        return iv, ciphertext


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


    # after work
    def decrypt(self, iv: str, ciphertext: str) -> str:
        if len(iv) != 16:
            raise ValueError("IV must be 16 characters.")

        ciphertext_blocks = [iv] + [ciphertext[index : index + self.n] for index in range(0, len(ciphertext), self.n)]
        output_blocks = []

        # Decrypt the data
        for index in range(len(ciphertext_blocks)-1, 0, -1):
            plaintext = self.black_xor_dec(self.black_box_dec(ciphertext_blocks[index]), ciphertext_blocks[index-1])
            output_blocks.insert(0, plaintext)
        return "".join(output_blocks)


    def black_xor_dec(self, data_1 : str, data_2 : str) -> str:
        blacktext = ""
        for pt_char, key_char in zip(data_1, data_2):
            black_char = ALPHABET[(ALPHABET.index(pt_char) - ALPHABET.index(key_char)) % len(ALPHABET)]
            blacktext += black_char 
        return blacktext

    def black_box_dec(self, data : str) -> str:
        blacktext_numbers = self.text_to_numbers(data)
        blocks = np.array(blacktext_numbers).reshape(-1, self.n)
        white_numbers = np.dot(blocks, np.array(self.inv_key).astype(np.int64)) % len(ALPHABET)
        return self.numbers_to_text(white_numbers.flatten())
    

# let's retrieve the key from [self.key.png]
key = np.array([[22,  8, 16, 15, 48,  3, 22, 12, 14, 39,  6,  7, 46, 16,  3,  1],
                [ 4, 42, 24, 29, 40, 17, 39, 40,  3,  7,  9, 28, 23,  4, 42, 29],
                [26, 46, 22, 26, 34, 35, 13, 28, 13, 20, 13,  7, 44, 38,  2,  4],
                [ 5, 33, 42, 12,  9, 15, 44, 24, 43, 27, 48, 13,  5,  1, 34, 27],
                [18, 39, 20, 35, 36,  0, 41, 25,  0,  7, 28, 37,  5, 19, 22, 42],
                [17, 11,  4, 18, 47, 14, 20, 42, 27, 48, 25, 29, 39, 28, 44, 37],
                [16, 38, 14, 26, 14, 33, 11, 18,  4, 41, 27, 22, 36, 24, 35,  0],
                [ 7, 34, 12, 27, 33, 10, 30, 11, 36, 33,  9, 33,  0, 44, 26, 37],
                [ 3,  8, 20, 35, 25, 48, 42, 42, 23, 26, 32, 15, 23, 23,  8, 25],
                [24, 48, 31, 41,  6, 39, 40, 41, 37, 27, 32, 41, 21,  8, 37,  8],
                [24, 19, 32, 25, 13, 39, 39, 45, 31, 32, 38, 30, 26, 20,  7, 29],
                [36, 15, 29, 23,  5, 31, 27, 33, 25, 34,  1, 42, 20,  1, 23,  4],
                [ 9, 26, 14, 15,  6, 13, 15, 13, 22,  5, 30, 22, 40,  6, 31, 11],
                [18, 42, 14, 44,  7, 15, 13, 39, 22,  0, 28, 41, 25, 13, 48,  8],
                [22, 16,  4,  8,  8, 31, 39, 40, 38,  9, 39, 38, 38, 40, 29, 19],
                [25, 42, 17,  7, 25, 28, 19, 45, 30, 26, 15, 33, 40,  3, 38, 21]])

# let's retrieve iv and ciphertext from [output.bin]
with open("output.bin", "rb") as file:
    iv, ciphertext = pickle.load(file)

cipher = AESCBC(key)
message = cipher.decrypt(iv, ciphertext)

print(message)
