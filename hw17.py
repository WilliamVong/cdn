"""
Team SWY - William Vongphanith, Vansh Shah, Julia Xue, Stanley Zheng
IntroCS pd6 sec10
HW17 - Cereal-Grade Encryption
2021-04-11
0.5 hrs
"""

def rot13_char(ch):
    if ord(ch) < ord("N") and ord(ch) >= ord("A"):
        return chr(ord(ch) + 13)
    elif ord(ch) <= ord("Z") and ord(ch) >= ord("N"):
        return chr(ord("A") + (ord(ch) - ord("N")))
    elif ord(ch) < ord("n") and ord(ch) >= ord("a"):
        return chr(ord(ch) + 13)
    elif ord(ch) <= ord("z") and ord(ch) >= ord("n"):
        return chr(ord("a") + (ord(ch) - ord("n")))
    else:
        return "invalid input"

def print_em_all():
    output = ""
    for ch in range(ord("A"),ord("Z") + 1):
        output += chr(ch) + " <=> " + rot13_char(chr(ch)) + "\n"
    output += "...\n"
    for ch in range(ord("a"),ord("z") + 1):
        output += chr(ch) + " <=> " + rot13_char(chr(ch)) + "\n"
    return output

def rot13_wrd(word):
    output = ""
    for ch in word:
        output += rot13_char(ch)
    return output
