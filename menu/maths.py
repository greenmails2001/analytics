import decimal


def find_lineAB(x1,y1, x2,y2, x_array):
    #print('y1: %s y2: %s' %(y1,y2))
    vectora = x2-x1
    vectorb = y2-y1
    #print(vectora)
    #print(vectorb)
    elementEnd = float(x_array[0])
    #print(elementEnd)
    y = [(vectorb*(elementEnd+float(i)+1-x1)/vectora+y1) for i,x in enumerate(x_array)]
    #print(y)
    return y
