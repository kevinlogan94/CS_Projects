#Kevin Logan
#Section 10

from math import *
def main():

    x1, y1=eval(input("Enter first point:"))
    x2, y2=eval(input("Enter second point:")) 
    distance=sqrt(((x2-x1)**2)+(y2-y1)**2)
    print("The distance is", distance)

main()
