# reverse and add
# encoding: utf-8
# python 3.6

import math

def reverseANDadd(x, count):
    reverse_x=int(str(x)[::-1])
    new_x=x+reverse_x
    count=count+1
    return new_x, count

def goORnot(str_x, floor_x):
    for i in range (1, floor_x+1):
        if (str_x[1*i-1]==str_x[-1*i]):
            continue
        else:
            return 0
    return 1

def main():
    y = input()
    y=int(y)
    for i in range (0, y):
        x = input()
        x=int(x)
        count=0
        while ((x<=4,294,967,295) or (count<1000)):
            str_x=str(x)
            len_x=len(str_x)
            floor_x=math.floor(len(str_x)/2)
            flag=goORnot(str_x, floor_x)
            if (flag==1):
                print (count, x)
                break
            else:
                x, count=reverseANDadd(x, count)

if __name__=="__main__":
        main()
