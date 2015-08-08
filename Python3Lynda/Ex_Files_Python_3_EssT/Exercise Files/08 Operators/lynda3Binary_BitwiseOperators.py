#!/usr/bin/python3


def b(n): print('{:08b}'.format(n)) #prints out binary value to 8 spaces


b(5)

x,y = 0x55, 0xaa
b(x)
b(y)
b(x|y)
b(x&y)
b(x^0) #exclusive or
b(x^0xff)
b(x << 4) #shifting left by 4 bits
b(x >> 4) #shifting right by 4 bits
b(~x) #compliment or unary operator
