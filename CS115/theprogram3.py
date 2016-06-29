#Program 3 prolog
# Kevin Logan
# October 18, 2012
# Section 10
# kmlo225@g.uky.edu
# Purpose: Play either 10 rounds of the game, Three dice, or run out of money trying. Each round you
#   input your bet and dice number and the program tells you if the dice you picked matches one of the
#   dice rolled. The amount of matches shows you how much money you win or lose. 
# preconditions: Input your bet and dice number. Take that information and plug it into several functions.
# postconditions: Output the how many dice matches you had with the dice you chose. Output 3 dice
#   drawings of the dice rolled. Output your winnings or losses. Repeat the process if you continue playing
#   the game.
###Design
    #FUNCTIONS#########
    #1       Drawdie1-6
    #purpose: draw the dice corresponding to its number
    #pre-conditions: None
    #post-conditions: Prints the die or for EXTRA CREDIT in turtle grpahics
    ####Design
    #Print top line of art
    #print second line
    #etc.
def dice1():
    print("+-----+")
    print("|           |")
    print("|     *     |")
    print("|           |")
    print("+-----+")
    

def dice2():
    print("+-----+")
    print("| *        |")
    print("|           |")
    print("|        * |")
    print("+-----+")

def dice3():
    print("+-----+")
    print("| *        |")
    print("|     *    |")
    print("|        * |")
    print("+-----+")

def dice4():
    print("+-----+")
    print("|   *  *   |")
    print("|           |")
    print("|   *  *   |")
    print("+-----+")

def dice5():
    print("+-----+")
    print("| *      * |")
    print("|     *    |")
    print("| *      * |")
    print("+-----+")


def dice6():
    print("+-----+")
    print("| *      * |")
    print("| *      * |")
    print("| *      * |")
    print("+-----+")

#2  draw
#purpose: call upon the previous functions to draw the correct die that was generated
#pre-conditions: what number was rolled
#post-conditions: calls other function
####Design
#if statements depending on roll to call the correct die
#if dice == 1:
#    die1()
#etc.

def draw(dice):
    if dice==1:
        dice1()
        
    if dice==2:
        dice2()
        
    if dice==3:
        dice3()
        
    if dice==4:
        dice4()
        
    if dice==5:
        dice5()

    if dice==6:
        dice6()

#3  picknum
#purpose: get correct number choice from user
#pre-conditions: None
#post-conditions: Forces the user to choose a number 1-6 and returns dicepick
####Design
#print please enter a number between 1 and 6 inclusive.
#receive input from user for dicepick
#while dicepick %1 !=0 or >=7 or <=0: ask to repick
#else return dicepick

def picknum():
    print("Please enter a number between 1 and 6 inclusive")
    dicepick=eval(input("Enter the number you want to bet on -->"))
    while dicepick % 1!=0 or dicepick <= 0 or dicepick >= 7:
        print("Sorry, that is not a good number")
        dicepick=eval(input("Enter the number you want to bet on -->"))
    else:
        return dicepick

#4  matches
#purpose: check if there are any matches
#pre-conditions: picknum and then what was rolled for the 3 dice.
#post-conditions: return the number of matches
####Design
#If no matches set the match to 0
#if picknum matches dice1 and dice2 and dice3 then match=3
#if picknum matches dice3 and dice1 or dice2 and dice3 or dice1 and dice2 then match=2
#if picknum matches only one dice1 or dice2 or dice3 then match=1
#return number of matches

def matches(picknum, dice1, dice2, dice3):
    if (dice1==picknum) and (dice2==picknum) and (dice3==picknum):
        match=3
        return 3
    elif (dice3==picknum and dice1==picknum) or (dice2==picknum and dice3==picknum) or (dice1==picknum and dice2==picknum):
           match=2
           return 2
    elif (picknum==dice1) or (picknum==dice2) or (picknum==dice3):
            match=1
            return 1
    else:
        match=0 
        return 0


#5     betting
#purpose: make sure they are betting a valid amount
#pre-conditions: total user can bet
#post-conditions: amount user is betting returned
####Design
#receive input from user, store as bet
#while bet <=0 or bet > stake
#if bet > stake they can't bet more than they have.
#receive input from user, store as bet
#else you cant bet 0 or less than zero
#receive input from user, store as bet
#return bet

def betting(stake):
        bet=eval(input("What is your bet?     "))
        while bet <= 0 or bet > stake:
            if bet > stake:
                 print("Sorry, you can't bet more than you have")
                 bet=eval(input("What is your bet?    "))
            else:
                 print("Sorry, you can't bet 0 or less than zero")
                 bet=eval(input("What is your bet?    "))
        return bet

#6     payoff
#purpose: find how much was won or lost
#pre-conditions: picknum bet dice1 dice2 dice3
#post-conditions: returns the payoff
####Design
#run previous function to find matches store as match
#if match equals 3, wager=bet*10, print that you got a triple match
#if match equals 2, wager=bet*5, print that you got a double match.
#if match equals 1, print that you got a match.
#if match equals 0, print that you lost your bet.
#return your payoff.

def payoff(picknum, bet, numrolled1, numrolled2, numrolled3):
    match=matches(picknum, numrolled1, numrolled2, numrolled3)
    if match==3:
        print("You got a TRIPLE match!")
        wager=bet*10
        print("You won $", wager, sep="")
        return bet*10
            
    elif match==2:
         print("You got a DOUBLE match!")
         wager=bet*5
         print("You won $", wager, sep="")
         return bet*5
                
    elif match==1:
        print("You got a match!")
        print("You won $", bet, sep="")
        return bet
                    
                    
    else:
        print("You lost your bet! $", bet, sep="")
        return bet

#7  playagain
#purpose: Play the game again if your stake is high than zero and if you want to.
#pre-conditions: flag and stake
#post-conditions: Repeat the program.
####Design
#if stake >0
#no equals "no"
#n equals "no"
#y equals "yes"
#yes equals "yes"
#input if u want to play again or not
#if what you inputted is y or yes then repeat the program.
#if you dont input y or yes then print goodbye.
def playagain(flag, stake):
    if stake >0:
        no="no"
        n="no"
        y="yes"
        yes="yes"
        keepplaying=eval(input("Want to play some more? "))
        if keepplaying!="yes":
                flag=False
        if flag==True:
            singles=0
            doubles=0
            triples=0
            misses=0
            rounds=1
            print()
            print("Play the game of Three Dice!!")
            print("You have", stake, "to bet with.")
            while stake > 0 and rounds <=10 and flag==True:
                    print("Round", rounds)
                    dice1=randrange(1, 7)
                    dice2=randrange(1, 7)
                    dice3=randrange(1, 7)
                    dicepick=picknum()
                    bet=betting(stake)
                    draw(dice1)
                    draw(dice2)
                    draw(dice3)
                    wager=payoff(dicepick, bet, dice1, dice2, dice3)
                    match=matches(dicepick, dice1, dice2, dice3)
                    singles, doubles, triples, misses = howmany(match, singles, doubles, triples, misses)
                    stake=final(match, stake, wager)
                    rounds+=1
                    print()
            print("***** Singles", singles," Doubles", doubles,"Triples", triples,"Misses", misses)
            print()
            playagain(flag, stake)
        else:
            print("Goodbye!")
        

#8  howmany
#purpose: Count and print the amount of singles, doubles, triples, and misses in your program.
#pre-conditions: match, singles, doubles, triples, misses
#post-conditions:the amount of each category and print it.
####Design
#If match equals zero, the amount of misses is increased by 1
#If match equals 1, the amount of singles is increased by 1
#If match equals 2, the amount of doubles is increased by 1.
#If match equals 3, the amount of triples is increased by 1.
#return singles, doubles, triples, misses

def howmany(match, singles, doubles, triples, misses):
    if match==0:
        misses+=1
        
    elif match==1:
        singles+=1
   
    elif match==2:
        doubles+=1
   
    elif match==3:
        triples+=1
    return (singles, doubles, triples, misses)


#9  final
#Purpose:Your new stake after each round of the game.
#Pre-condition:match, money, wager
#post-condition:Your new increased stake if you win or your new decreased stake if you lose.
####Design
#if match is greater than zero, increase money by the wager amount, print it,assign stake to money, then return it.
#elif match==0 then decrease money by the wager.
#if your money is less than or equal to zero, print your new stake, print game over, and return stake.
#else print your new stake, assign stake to money, return stake.

def final(match, money, wager):
        if match > 0:
            money+=wager
            print("Your stake is $", money,sep="")
            stake=money
            return stake

        elif match==0:
            money-=wager
            if money <= 0:
                print("Your stake is $0")
                print("Game Over!!!")
                stake=0
                return stake

            else:
                print("Your stake is $", money, sep="")
                stake= money
                return stake


#10 input the random library. This library generates the random dice rolled.
from random import *

def main():
    #11 Opening Message
    print("Play the game of Three Dice!!")
    #12 State how much you have to bet on.
    print("You have $1000 to bet with.")
    #13 Input the amount you have to bet on.
    stake=1000
    #14 Assign singles to zero.
    singles=0
    #15 Assign doubles to zero.
    doubles=0
    #16 Assign triples to zero.
    triples=0
    #17 Assign misses to zero.
    misses=0
    #18 Assign rounds to one.
    rounds=1
    #19 Assign True to flag.
    flag=True
    #20 Make a loop that continues if stake > 0 and rounds <= 10 and flag==True.
    while stake >0 and rounds <=10 and flag==True:
            #21 Print the round.
            print("Round", rounds)
            #22 Assign dice1 a random number between 1 and 6.
            dice1=randrange(1, 7)
            #23 Assign dice2 a random number between 1 and 6.
            dice2=randrange(1, 7)
            #24 Assign dice3 a random number between 1 and 6.
            dice3=randrange(1, 7)
            #25 Assign dicepick to the return integer of picknum
            dicepick=picknum()
            #26 Assign bet to the returned integer of betting
            bet=betting(stake)
            #27 Draw the first random dice.
            draw(dice1)
            #28 Draw the second random dice.
            draw(dice2)
            #29 Draw the third random dice.
            draw(dice3)
            #30 Assign wager to the returned integer of payoff.
            wager=payoff(dicepick, bet, dice1, dice2, dice3)
            #31 Assign match to the returned integer of matches.
            match=matches(dicepick, dice1, dice2, dice3)
            #32 Assign singles, doubles, triples, and misses to the returned amount of singles, doubles, triples, and misses.
            singles, doubles, triples, misses = howmany(match, singles, doubles, triples, misses)
            #33 Assign stake to the integer returned by final.
            stake=final(match, stake, wager)
            #34Increase rounds by 1
            rounds+=1
            #35 Print a blank line
            print()
    #36 Print the singles, doubles, triples, and misses.
    print("***** Singles", singles," Doubles", doubles,"Triples", triples,"Misses", misses)
    #37 Print a blank line.
    print()
    #38 Input function to repeat the game if you want it to.
    playagain(flag, stake)
   
    


main()
