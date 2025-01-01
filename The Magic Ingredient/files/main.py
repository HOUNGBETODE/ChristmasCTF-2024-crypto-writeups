from cb32 import encode
from secret import FLAG

with open("message", "wb") as file:
    file.write(encode(FLAG))