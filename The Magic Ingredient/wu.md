- The main goal was about understanding the logic of the function **encode** and finding a way to get the flag.

- What did **encode** do ?
  - it generates an alphabet based on a random seed
  - it then converts the given __plaintext__ into binary
  - it finally groups the binaries five by five and associates the decimal value corresponding to a group of 5 bits with the character occupying that position in the generated alphabet

- Once the process is understood, it's easy to reverse it. Nevertheless, we still need to guess the correct alphabet.

- Looking at the __main.py__ file, a hint was found: **__message__ was modified before encode was applied**. Thus, the time taken to modify __message__ is less than the time used by the seed. In other words, simply extract the modification time of __message__ and increment it until you reach the value of the seed.

- Flag was : **CMCTF{c0ngr@ts_y0u'r3_1nd33d_@_b@s3_r3v3rs3r_51e2e1e0be491d}**.