#Kevin Logan
#Section 10
#Lab10
#Kmlo225@g.uky.edu
#October 25, 2012

def main():
    flag=True
    num1=eval(input("Enter number 1: "))
    i=2
    while i < 9:
            print("Enter number", end=" ")
            print(i, end="")
            num2=eval(input(": "))
            if num1 > num2:
                flag=False
                num1=num2
            i+=1
    if flag==True:
        print()
        print("yes")
    else:
        print()
        print("no")

main()
        
 #This program tells you whether the second number you put in is larger than the first.            
#If the output is yes then the second number is larger than the first.
#If the output is no then the first number is larger than the second. The second value is then
#put into the variable for. 
