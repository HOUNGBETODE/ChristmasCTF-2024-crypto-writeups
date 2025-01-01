given_string = "-.----..-.--..-.-.----..-.-.-.---.---..--....-..-..---..-..-.----..--.-.-..--.-.-...--.--.-.....-...-.-.-...-----.-.....-..--.---...-.-.-..--.---..--.-.--.----.--...-.---......--.-.-.--.....-."

probes = [
    {".": "0", "-": "1"},
    {".": "1", "-": "0"}
]

back_to_ascii = lambda bin_ : "".join(chr(int(bin_[index:index+8], 2)) for index in range(0, len(bin_), 8)) if not bool(len(bin_)%8) else None

for try_ in probes:
    ascii_pattern = back_to_ascii(
        given_string.translate(
            str.maketrans(try_)
        )
    ) 
    if "CMCTF" in ascii_pattern:
        print(ascii_pattern)