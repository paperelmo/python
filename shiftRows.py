# shiftRows 4X4
# python 3.7
# 20190105
def shiftRows():
    state=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tmp=[]
    for i in range (0,4):
        for j in range (0, 4):
            count=4*i+5*j
            if (count<16):
                tmp.append(state[count])
            else:
                tmp.append(state[count-16])
    for k in range (0, 16):
        state[k]=tmp[k]
    print (state)

shiftRows()
