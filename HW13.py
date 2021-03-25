#Pyfun -- William Vongpanith, Maggie Huang, and Felix Bento
#IntroCS pd06 sec10
#HW13 -- Applying Our Tools
#2021-03-25

#Finds the Sum of the Digits in the Input
def sum_digits(n):
    digits_gunky = list(str(n))
    digits = [ digit for digit in digits_gunky if digit.isdigit() ]
    i = 1
    output = 0
    while i <= len(digits):
        output += int(digits[i - 1])
        i += 1
    return output
    
print(sum_digits(1357)) #16
print(sum_digits(13579)) #25
print(sum_digits(6667)) #25
print(sum_digits(45.678)) #30
print(" ")

#Finds The Squares of every integer between 1 and n
def squares(n):
    i = 1
    output1 = ""
    while i < n:
        output1 += "" + str(i) + ": " + str(i ** 2) + "\n"
        i += 1
    output1 += "" + str(n) + ": " + str(n ** 2) + "\n"
    return output1
        
print(squares(5)) #1, 4, 9, 16, 25
print(squares(15)) #1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225
print(squares(17)) #1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289

#Finds Every integer that is a Perfect Square Between n and 1   
#Finds Every integer that is a Perfect Square Between n and 1  and adds them
def sum_perf_sqs(n):
    output2 = 0
    while n > 1:
        if (n ** 0.5) % 1 == 0:
            output2 +=  n
            n = n - 1
        else:
            n = n - 1
    return output2 + 1

print(sum_perf_sqs(5)) #4, 1
print(sum_perf_sqs(16)) #16, 9, 4, 1
print(sum_perf_sqs(37)) #36, 25, 16, 9, 4, 1

#Prints a string of the Addition of a and b and the Product of a and b
def add_mult_print(a,b):
    n = a + b
    m = a * b
    return 'the sum of ' + str(a) +  ' and ' + str(b) + ' is ' + str (n) + ('\n') + 'their product is ' + str(m)

print(add_mult_print(3,6)) #9, 18
print(add_mult_print(2,2)) #4, 4
print(add_mult_print(1,10)) #11, 10

#Prints a HTML code of the Addition of a and b and the Product of a and b
def add_mult_html(a,b):
    n = a + b
    m = a * b
    return 'the <i>sum</i> of ' + str(a) +  ' and ' + str(b) + ' is <b>' + str (n) + ('\n') + '</b>their <i>product</i> is <b>' + str(m) + '</b>'

print(add_mult_html(3,6)) #9, 18
print(add_mult_html(2,2)) #4, 4
print(add_mult_html(1,10)) #11, 10

#returns html code of a table of every integer, its square and the sum of its digits up to and including n
def tablefy (n):
    i = 1
    output1 = ''
    while i < n:
        output1 += "<tr>" + '\n' + "<td>" + str(i) + "</td>" +'\n' + "<td>" + str(i**2) + "</td>" + '\n' + "<td>" + str(sum_digits(i)) + "</td>" + '\n' + "</tr>" + '\n'
        i = i + 1
    output1 += "<tr>" + '\n' + "<td>" + str(n) + "</td>" +'\n' + "<td>" + str(n**2) + "</td>" + '\n' + "<td>" + str(sum_digits(n)) + "</td>" + '\n' + "</tr>" + '\n' 
    return '<table>' + '\n' + "<tr>" + '\n' + "<td>" + 'n' + "</td>" +'\n' + "<td>" + 'n^2' + "</td>" + '\n' + "<td>" + 'sumDigits' + "</td>" + '\n' + "</tr>" + '\n' + str(output1) + '</table>'

print (tablefy (10)) #1 1 1, 2 4 4, 3 9 9, 4 16 7, 5 25 7, 6 36 9, 7 49 13, 8 64 10, 9 81 9, 10 100 1