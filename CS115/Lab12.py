#Kevin Logan
#Section 10
#Lab 12

def main():
    word=input("Enter a string:  ")
    for i in range(0,len(word),2):
        print(word[i], end="")
    print()

    for i in range(len(word)-1, 0-1, -1):
        print(word[i], end="")
    print()
    
    if len(word) <= 5:
        print("short")
    else:
        print(word)

    if len(word) >=4:
        newword=(word[:2] + word[-2:])
        print(newword)
    else:
        newword=word
        print(newword)

    if newword[-2:] == "es":
        newword2=word + "ies"
        print(newword2)
    else:
        newword2= word + "es"
        print(newword2)
        
main()
