from time import time
from typing import Any, Optional
from random import choice, seed, shuffle
from string import ascii_letters, digits, punctuation

alphabet = list(punctuation + digits + ascii_letters)

def genAlphabet() -> str:
    global alphabet
    seed(int(time()))
    shuffle(alphabet)
    return "".join(alphabet[:32]).encode()

encode = lambda plaintext : (cryptic_alphabet:=genAlphabet()) and (transtext:="".join(bin(ord(char))[2:].zfill(8) for char in (plaintext + chr(choice(cryptic_alphabet)) * ((len(plaintext) * 8) % 5)))) and bytes(cryptic_alphabet[int(transtext[counter:counter+5], 2)] for counter in range(0, len(transtext), 5))

def decode(**kwargs) -> Optional[bytes]: return None