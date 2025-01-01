- The CIA intern hired by Santa Claus made a very serious mistake: "__he rewrote AES-CBC using known algorithms that are reversible at every level__".

- If you pay close attention, you'll notice that **black_xor was vigenère** and **black_box was Hill encryption**. So it was trivial to rewrite the inverse components.

- Taking a closer look at the __AESCBC.png__ file, it becomes easy to write the decrypt function

- All this together gives us the flag : **CMCTF{0h_5h1t_th15_3nc0d1ng_w45_n0t_54f3_4t_4ll!}**.