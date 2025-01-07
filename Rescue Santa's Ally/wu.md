- Here, we needed to do a little research into the mechanism for reconstituting path bits p and q in RSA.

- After a bit of research, we came across this document (https://eprint.iacr.org/2020/1506.pdf) which talks about this in section (**4.3.1 Random known bits of p and q**). The reconstitution mechanism is described on page 22.

- However, in the document, this was done in base 2, but the challenge integers were supplied in base 10, so the solution will have to be adapted.

- To make things a little trickier, 3 digits of the n have been obfuscated. Brute-forcing 3 elements in a series of 10 elements is achievable in record time.

- Once the integers p and q have been reconstituted, we notice that __$$ GCD(e, phi) \neq 1 $$__
This is a problem commonly referred to as **roots of unity**.  The article (https://brilliant.org/wiki/roots-of-unity/) details this concept.

- All this was pooled to produce the final flag.

- Flag was : **CMCTF{Gr34t_J0b_R3c0n5truct1ng_Th4t_S4nt4_Cl4u5_Puzzl3!}**.