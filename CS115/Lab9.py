# Kevin Logan
# October 18, 2012
# Section 10

def leapyear(y):
    if y % 4 == 0:
       if y % 100 != 0:
            print("yes, it is a leap year")
       if y % 100==0:
           if y % 400==0:
            print("yes, it is a leap year")
           else:
            print("no, it is not a leap year")
    else:
        print("no, it is not a leap year")
    
    

def main():


    year=eval(input("Enter a year: "))

    leapyear(year)

main()
