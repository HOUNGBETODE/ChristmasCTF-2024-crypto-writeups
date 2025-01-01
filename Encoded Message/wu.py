from math import sqrt

def find_real_word(secretWord):
    matrixSize=int(sqrt(len(secretWord)))
    listeChars=list()
    for i in range(0, len(secretWord), matrixSize):
        listeChars.append(list(secretWord[i:i+matrixSize]))
    realWord += "".join(k[-j] for j in range(1, matrixSize+1) for k in listeChars)
    return realWord

print(find_real_word('sI_hsmydM__41ty__yFbns__yR_03d_gg00br__X1rus33ym-f3_3lv04mt4b_03uy4_t3mvrr_st3_43'))
