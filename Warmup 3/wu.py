from base64 import b64decode

fish_grave = 615687771126612277118786890525687771071001229812010787781187084971205687771126610677118706890120691229812081109781187068901225687771077484771187084971207312298120811097712156877711290122981208171771205687771129010677118706890121568777107788477118708497496912298120107109775056877710774106781187068905069122981201077179118706890121568777107821229812010710977120568777112741229812081877812056877710770122981201071097711874689012156877711274847711870689048731229812010750774956877710782847711870849751691229812081717712056877711266847711870849712277887710770122991201075077

def ascii_code(code : int) -> str:
    answer = int_ = ""
    for digit in str(code):
        int_ += digit
        if int(int_) in range(32, 127):
            answer += chr(int(int_))
            int_ = ""
    return answer

def str_development(string):
    answer = factor = ""
    for char in string:
        try:
            temp = int(char)
        except:
            answer+=char*int(factor)
            factor = ""
        else:
            factor += char
    return answer

def deadfish_interpreter(code):
    acc = 0
    output = []
    for cmd in code:
        if cmd == 'i':
            acc += 1
        elif cmd == 'd':
            acc -= 1
        elif cmd == 's':
            acc **= 2
        elif cmd == 'o':
            output.append(acc) 
    return output

flag = "".join([
    chr(i) for i in deadfish_interpreter(
        str_development(
            b64decode(
                ascii_code(
                    fish_grave
                )[::-1]
            ).decode()
        )
    )
])
print(f"{flag = }")