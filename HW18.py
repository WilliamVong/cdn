"""
Team SWY - William Vongphanith, Julia Xue
IntroCS pd6 sec10
HW18 - Crak'n Crunch
2021-04-13
0.4 hrs

Approach to the challenge:
We refactored the code from last homework to
create the rot13 function and used rot13_char
as a helper function. We also changed rot13_char
so someone can adjust by how much the function shifts
a letter through changing the shift variable, and
then we ran the code with different values of shift to see
which ones decoded the words.
"""

def rot13_char(ch):
# takes a letter and returns its rot13 equivalent 
# (the letter 13 letters after the letter)
    shift = 13
    if ord(ch) >= ord('a') and ord(ch) <= ord("z"):
        offset = ord('a')
        return chr(((ord(ch)-offset+shift)% 26)+offset) 
    elif ord(ch) >= ord('A') and ord(ch) <= ord("Z"):
        offset = ord('A')
        return chr(((ord(ch)-offset+shift)% 26)+offset)
    return None

def rot13(phrase):
# takes a string, which might have punctuation, and returns its rot13 equivalent
    output = ""
    for ch in phrase:
        if rot13_char(ch) == None:
            output += ch
        else:
            output += rot13_char(ch)
    return output

print(rot13("Justin Bieber")) # -> "Whfgva Ovrore"
print(rot13("Justin Bieber? Like, OMG!!! He's my hero!")) # -> "Whfgva Ovrore? Yvxr, BZT!!! Ur'f zl ureb!"
print(rot13("deoh, ufwyd, udm"))
# deoh is able shifted 23 to the left (3 to the right)
# ufwyd is party shifted 21 to the left (5 to the right)
# udm is fox shifted 11 to the left (15 to the right)

import enchant as Enchant
d = Enchant.Dict("en_US")

"""
I made a function that would be able to shift 
letters by a specified amount, in the function "rot". 
I also implemented a function named "rot_check" 
that in one line, would check if the character could 
be rotated by 13. 
Also, to quickly un-rot any word given, I created 
a function that would get every scrambling of the input
and then check if one or more of these scramblings 
were a real word. I used the Enchant library to assist
with this. 
Please check https://replit.com/@WilliamVongphan/rotter
to see the program in action.
"""

def rot(ch, n):
    if ord(ch) >= ord("A") and ord(ch) <= ord("Z"):
        offset = ord("A")
    elif ord(ch) >= ord("a") and ord(ch) <= ord("z"):
        offset = ord("a")
    else:
        return None
    return chr((((ord(ch) - offset) + n) % 26) + offset)

def rot_check(ch):
    return True if ord(ch) <= ord("Z") and ord(ch) >= ord("A") or ord(ch) <= ord("z") and ord(ch) >= ord("a") else False

def rotter(thing1):
    output_list = ""
    mylist = []
    for i in range(26):
        output = ""
        for ch in thing1:
            if rot_check(ch) == True:
                output += rot(ch, i)
            else:
                output += ch
        output_list += output + " -> shifted " + str(i) + " to the right,\n"
        mylist.append(output)
    newthing = ""
    for thing in mylist:
        if d.check(thing) == True:
            newthing += thing + "\n"
    if newthing == "":
        print("no matches for " + thing1)
    else:
        print(newthing)
# Extra: William's Rotter ("un-rot any word magically")
# https://replit.com/@WilliamVongphan/rotter
