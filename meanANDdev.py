# mean and standard deviation
# encoding: utf-8
# python 3.6

import math

def square(x):
    square_x=x*x
    return square_x

def mean(num_list):
    num_len=len(num_list)
    sum=0
    for num in num_list:
        sum=sum+num
    num_mean=sum/num_len
    return num_mean

def dev(num_list, num_mean):
    square_list=[]
    num_len=len(num_list)
    for num in num_list:
        square_result=square(num-num_mean)
        square_list.append(square_result)
    square_sum=0
    for square_num in square_list:
        square_sum=square_sum+square_num
    diff=(1/num_len)*square_sum
    dev_result=math.sqrt(diff)
    return dev_result

def main():
    y = input()
    y=int(y)
    num_list=[]
    while (y>0):
        x = input()
        x=int(x)
        num_list.append(x)
        y=y-1
    num_mean=mean(num_list)
    dev_result=dev(num_list, num_mean)
    print (num_mean, ',', dev_result)

if __name__=="__main__":
        main()
