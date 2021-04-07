'''
Team HAV: William Vongphanith, Hana Kaloudis
IntroCS pd6 sec10
HW16: For ASCII Tablefication 
2021-04-07
time cost: 0.7 hrs
'''

def tablefy_ascii():
    # Design stuff to make table look nicer, as well as the headers for the table
    output = "<style>table, th, td {border: 1px solid black;width: 100px;border-collapse: collapse;padding:5px}</style><table><th>Character</th><th>Value</th>"
    # Uppercase letters
    for char in range(65,91):
        output += "<tr><td>" + chr(char) + "</td><td>" + str(char) + "</td></tr>"
    # Lowercase Letters
    for char in range(97,123):
        output += "<tr><td>" + chr(char) + "</td><td>" + str(char) + "</td></tr>"
        # Return the stuff, with the ending
    return output + "</table>"

print(tablefy_ascii())
