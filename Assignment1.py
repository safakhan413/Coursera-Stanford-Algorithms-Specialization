
def karatsuba_mult(x,y):
    if x<100 or y<100: return x*y
    x = str(x); y = str(y);
    # convert to string of 0/1's, MSB first
    n = max(len(x),len(y))
    x = "0"*(n-len(x))+x; y = "0"*(n-len(y))+y # add leading zeroes if needed
    print('x is: ' ,x)
    print('y is: ' ,y)

    m = n//2
    xtop = int(x[:-m]); xbot = int(x[-m:])
    ytop = int(y[:-m]); ybot = int(y[-m:])
    return (10**(2*m)-10**m)*karatsuba_mult(xtop,ytop)+(10**m)*karatsuba_mult(xtop+xbot,ytop+ybot) +(1-10**m)*karatsuba_mult(xbot,ybot)


x= 314
y = 271828
print(karatsuba_mult(x,y))