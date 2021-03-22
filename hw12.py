'''
William Vongphanith
IntroCS pd6 sec10
HW12 - Implementation
2021-3-18
Time cost: 2 minutes (I did this for previous assignment)
'''

def closer_num(target, num1, num2):
    try:
        diff1 = abs(target - num1)
        diff2 = abs(target - num2)
        if diff1 < diff2:
            return str(target) + " is closer to " + str(num1)
        elif diff2 < diff1:
            return str(target) + " is closer to " + str(num2)
        else:
            return str(target) + " is the same distance between " + str(num1) + " and " + str(num2)
    except:
        return ("Invalid Data Type")
        
print(closer_num(2,5,10))
print(closer_num(2,5,3))
print(closer_num(2,5,5))
print(closer_num(-4,5,10))
print(closer_num(2,5.7,10.9990))
print(closer_num(2,5,"foo"))

def grade_conv(g):
    try:
        if g >= 90 and g <= 100:
            return "A"
        elif g >= 80 and g < 90:
            return "B"
        elif g >= 70 and g < 80:
            return "C"
        elif g >= 65 and g < 70:
            return "D"
        elif g >= 0 and g < 65:
            return "F"
        elif g < 0:
            return "Yikes! That's a bad grade!"
        elif g > 100:
            return "This class doesn't have extra credit!"
    except:
        return ("Invalid Data Type")

print(grade_conv(99))
print(grade_conv(90))
print(grade_conv(85))
print(grade_conv(75))
print(grade_conv(65))
print(grade_conv(24.4444777))
print(grade_conv(110))
print(grade_conv(-3))
print(grade_conv("bar"))

def pass_judgement(input):
    grade = str(input).upper()
    if grade == "A":
        return "Great job! You got an A!"
    elif grade == "B":
        return "Good job. You got a B"
    elif grade == "C":
        return "That's ok, just study more next time. You got a C"
    elif grade == "D":
        return "Try harder next time, you got a D"
    elif grade == "F":
        return "You absolute failure, you got an F!"
    else:
        return ("\n\n---\nThat's not valid input! The grade should be an A, B, C, D, or F. Input: " + str(grade) + "\n---\n\n")
        
print(pass_judgement(grade_conv(99)))
print(pass_judgement(grade_conv(90)))
print(pass_judgement(grade_conv(85)))
print(pass_judgement(grade_conv(75)))
print(pass_judgement(grade_conv(65)))
print(pass_judgement(grade_conv(24.4444777)))
print(pass_judgement(grade_conv(110)))
print(pass_judgement(grade_conv(-3)))
print(pass_judgement(grade_conv("bar")))
print(pass_judgement("A"))
print(pass_judgement("b"))
print(pass_judgement(88))

