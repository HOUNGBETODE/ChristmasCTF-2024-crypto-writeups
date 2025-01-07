from skimage.io import imread

# here we convert back the image to it's pixels array
flag_pixels_array = (
    imread(fname="./files/flag.png", as_gray=True)
    .astype(int)
)

# only two values appear: 0 and 1 are found
# this is a clue to the binary stuff
# decoding the binary sequence as it was doesn't give us anything significant (®ÏÎ“ ©º¥È±Í§Ì”±±§¾ºÌ§½§Ï±¹¸ÏÏ±©ÇÏ¦½Î±ÎÆ±-¶µÇÎ"²¨Ê®ÂÂÂ)
# let's try to invert each bit by repeating the decoding process
bin2char = (
    "".join(
        chr(
            int("".join([str(bit) for bit in bits]), 2)
        ) 
        for bits in 1-flag_pixels_array
    )
)

# we got something very close to base64 encoding
# let's decode it to see whether it's worth our while doing
from base64 import b64decode
message = b64decode(bin2char).decode()

print(message)