#!/usr/bin/env python3

def happy_new_year():

    for i in range(10,0,-1):
    #   if i == 1 :
    #     print ("Happy New Year!")
    #   else:
        print(i) 
    print("Happy New Year!")
    # return  0
 
    # code goes here!
#     pass
# print(happy_new_year()) 
def square_integers(int_list):
    # code goes here!
    set_list=[]
    for i in int_list:
        # if i > 0:
        set_list.append(i*i)
        # else:
        #     print("number is less than o")
    return set_list

# print(square_integers([1,2,3]))
    # pass

def fizzbuzz():
    # code goes here!
    for n in range(1,101):
        if n % 15 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)
    return ("invalid")
        
# print(fizzbuzz(45))
