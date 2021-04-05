#Pyfun -- William Vongpanith, Maggie Huang, and Felix Bento
#IntroCS pd06 sec10
#HW14 -- PPMP
#2021-03-25
#Time Cost:

#-----------   String-1   -----------------

#1 hello_name
def hello_name(name):
    return 'Hello ' + name + "!"

'''print (hello_name('Bob'),  '... should be Hello Bob!')
print (hello_name('Alice'), '... should be Hello Alice!')
print (hello_name('X'), '... should be Hello X!')
print ('\n')'''


#2 make_abba
def make_abba(a, b):
    return a + b + b + a

'''print (make_abba('Hi', 'Bye') , '... should be HiByeByeHi')
print (make_abba('Yo', 'Alice') , '... should be YoAliceAliceYo')
print (make_abba('What', 'Up') , '... should be WhatUpUpWhat')
print ('\n')'''


#3 make_tags
def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

'''print (make_tags('i', 'Yay'), '... should be <i>Yay</i>')
print (make_tags('i', 'Hello') , '... should be <i>Hello</i>')
print (make_tags('cite', 'Yay') , '... should be <cite>Yay</cite>')
print ('/n')'''


#4 make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:4]

'''print (make_out_word('<<>>', 'Yay') , '... should be <<Yay>>')
print (make_out_word('<<>>', 'WooHoo'),  '... shoul be <<WooHoo>>')
print (make_out_word('[[]]', 'word') , '... should be [[word]]')
print ('\n')'''


#5 extra_end
def extra_end(str):
    return str[-2:] + str[-2:] + str[-2:]

'''print (extra_end('Hello') , '... should be lololo')
print (extra_end('ab') , '... should be ababab')
print (extra_end('Hi'),  '... should be HiHiHi')
print ('\n')'''


#6 first_two
def first_two(str):
    return str[:2]

'''print (first_two('Hello') , '... should be He')
print (first_two('abcdefg'),  '... should be ab')
print (first_two('ab') , '... should be ab')
print ('\n')'''


#7 first_half
def first_half(str):
    return str[:len(str) // 2]

'''print (first_half('WooHoo') , '... should be Woo')
print (first_half('HelloThere'),  '... should be Hello')
print (first_half('abcdef') , '... should be abc')
print ('\n')'''


#8 without_end
def without_end(str):
    end = len(str) - 1
    return str[1: end]

'''print (without_end('Hello') , '... should be ell')
print (without_end('java'),  '... should be av')
print (without_end('coding') , '... should be odin')
print ('\n')'''


#9 combo_string
def combo_string(a, b):
    if len(a) > len(b):
      return b + a + b
    return a + b + a

'''print (combo_string('Hello', 'hi') , '... should be hiHellohi')
print (combo_string('hi', 'Hello') , '... should be hiHellohi')
print (combo_string('aaa', 'b') , '... should be baaab')
print ('\n')'''


#10 non_start
def non_start(a, b):
    return a[1:] + b[1:]

print (non_start('Hello', 'There') , '... should be ellohere')
print (non_start('java', 'code') , '... should be avaode')
print (non_start('shotl', 'java'),  '... should be hotlava')


#11 left2
def left2(str):
    return str[2:] + str[:2]

'''print (left2('Hello') , '... should be lloHe')
print (left2('java') , '... should be vaja')
print (left2('Hi') , '... should be Hi')
print ('\n')'''


#--------------- Logic-2 ---------------------

#1 make _bricks
def make_bricks(small, big, goal):
    if small + (5 * big) >= goal:
        if small >= goal % 5:
            return True
        return False
    return False

'''print (make_bricks(3, 1, 8), '... should be True')
print (make_bricks(3, 1, 9), '... should be False')
print (make_bricks(3, 2, 10) ,'... should be True')
print ('\n')'''

#2 lone_sum
def lone_sum(a, b, c):
    n = a + b + c
    if n == 3 * a:
      return 0
    if a == b or a == c:
      return n - (2 * a)
    if b == c:
      return a
    return n


#3 lucky_sum
def lucky_sum(a, b, c):
    n = a + b + c
    if a == 13:
      return 0
    if b == 13:
      return a
    if c == 13:
      return a + b
    return n

#4 no_teen_sum
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  if n >= 13 and n <= 19:
    if n == 15 or n == 16:
      return n
    else: 
      return 0
  else:
    return n

#5 round_sum
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  return (num//10)*10 if num%10<5 else (num//10)*10+10

#6 close_far
def close_far(a, b, c):
  return True if abs(a-b)<=1 and (abs(a-c)>1 and abs(b-c)>1) or abs(a-c)<=1 and (abs(a-b)>1 and abs(b-c)>1) else False

#7 make_chocolate
def make_chocolate(small, big, goal):
  bigneed = goal // 5
  if big > bigneed:
    if small >= goal - bigneed * 5:
      return goal - bigneed * 5
    else:
      return -1
  elif big <= bigneed:
    if small >= goal - big * 5:
      return goal - big * 5
    else: 
      return -1
