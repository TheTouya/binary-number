import math
number = str(input())
the_list = []
remainder = []
def showing_number(number):
    for x in range(len(number)):
        print("hello")
def division(num, base):
    the_base = base
    global the_list
    global remainder
    remainders = ''
    if num >= base:
       the_list.append(math.floor(num / the_base))
       remainder.append(num % the_base)
       division(math.floor(num / the_base), the_base)
    if num < base:
        divisions = str(the_list[-1])
        for x in reversed(remainder):
            remainders += str(x)
        final_number = divisions + remainders
        print(final_number)

        
       
division(int(number.split()[0]), int(number.split()[1]))