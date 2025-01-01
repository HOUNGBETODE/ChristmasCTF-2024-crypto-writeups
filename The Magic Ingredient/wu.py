from os.path import getmtime
from random import seed, shuffle
from string import ascii_letters, digits, punctuation

message_file = "files/message"
seed_ = int(getmtime(message_file)) # modification time extraction
alphabet = list(punctuation + digits + ascii_letters)
message_bin = open(message_file, "rb").read()

iterator = 0
while True:
    seed(seed_ + iterator)
    alphabet_in_use = alphabet[:]
    shuffle(alphabet_in_use)
    cryptic_alphabet = "".join(alphabet_in_use[:32]).encode()
    try:
        # the two next following lines were used to reverse the function ""encode""
        transform = "".join(bin(number)[2:].zfill(5) for number in [cryptic_alphabet.index(char) for char in message_bin])
        message = bytes([int(transform[index:index+8], 2) for index in range(0, len(transform), 8)]).decode()
        if "CMCTF{".lower() in message.lower():
            print(f"{message = }")
            break
    except:
        continue
    iterator+=1