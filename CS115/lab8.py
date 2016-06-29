# Kevin Logan
# Section 10
# October 11, 2012
# kmlo225@g.uky.edu

def main():
    cost=0
    y=5
    n=6
    print("Enter your choices as y or n.")
    mowing=eval(input("Do you want Basic Lawn Mowing? ")) 
    if mowing == 5:
            cost+=20
    trimming=eval(input("Do you want Trimmig and Sweeping? "))
    if trimming==5:
            cost+=25
    cleaning=eval(input("Do you want Pool Cleaning? "))
    if cleaning==5:
            cost+=50
    plants=eval(input("Do you want Watering Plants? "))
    if plants==5:
            cost+=10
    print()

    print("The total for your services is $", cost, sep="")
    print("Thank you for your business!")

main()
