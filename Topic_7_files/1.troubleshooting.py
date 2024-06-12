#! /usr/bin/env python3

""" Troubleshooting Python3 """

import sys

## Function
def tp_fun(required, *args, *kwargs):
    """ My Function """

    print("required:  {type(required)}  {required}\n")
    if (args):
        print(f"args:  {type(args}  {args}\n")
    if (kwargs):
        print(f"kwargs:  {type(kwargs}  {kwargs}\n")
    return([required, args, kwargs])

    # End function tp_function()

## main program
if (len(sys.argv) == 5):
    (_,a,b,c,d) = sys.argv
else:
    print(f"\nERROR: Supply four values please\n"
          f"~$ {sys.argv[0]} <val 1> <val 2> "
          f"<val 3> <val 4>\n")

list_ = tp_fun(a,b,c,d,m==1,n==2,o==3,p==4)
for x in list_:
    print("{x}\n")
 
sys.exit()
