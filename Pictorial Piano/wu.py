# here we convert back the image to it's pixels array
from skimage.io import imread
flag_pixels_array = imread("flag.png")

# only two pixels appears : [0 0 0] and [255 255 255] are found
# this is a clue for binary stuff
# surely [0 0 0] probes for 1 and [255 255 255] probes for 0, or vice versa
# let's pursue with the first hypothesis : [0 0 0] => 1 and [255 255 255] = 0
# with this is mind, let's extract the binary content obfuscated
import numpy as np
bin_digits = ""
for array_2d in flag_pixels_array:
    for pixel in array_2d:
        bin_digits += "0" if np.array_equal(pixel, np.array([255,255,255])) else "1"

# now we try to decode that binary sequence to see whether it's understandable
bin2char = ""
for i in range(0, len(bin_digits), 8):
    bin2char += chr(int(bin_digits[i:i+8], 2))

# we got something very close to base64 encoding
# let's decode it to see whether it's worth our while doing
from base64 import b64decode
message = b64decode(bin2char).decode()

print(message)