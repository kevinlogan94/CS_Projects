# Program 5
# Kevin Logan
# Section 10
# December 6 2012
# kmlo225@g.uky.edu
# purpose: to simulate a small subset of a domain name server's
#    actions, manage a list of domain names and IP numbers
#    with information added, new entries added, queries answered
# Preconditions: You input a your command file, "=" to use SET, a " ? " to use ASK, or a " * " to use SHOW.
#       You then write domain name and ip number after "=", write ip number or domain name after " ? ",
#       and you dont write anything with " * ". Everything for SET, ASK, and SHOW are in the command file.
# Postconditions:  If you use a "=" and a ipnumber and domain name it uses SET. If you
#       dont have the ip number but the domain name in the txt file, it replaces the domain names ip
#       number with the new ip number you entered. If you dont have the domain name in the txt file
#       then it inserts the ip number and domain name for you. It displays the total entries in the txt
#       file.
#       If you use a " ? " and an ip number, it tells you the ip number that the domain name it's assigned
#       to. If you use a " ? " and a domain name, it tells you the domain name and the ip number it's
#       assigned to.
#       If you use a " * " then it shows all the domain names and ip numbers in the txt file.
####Functions####
# Function name: gettable
# Purpose: a function responsible for getting the information from the dnstable file and putting
#       it into two lists, one for domain names and one for IP numbers. It returns the two lists through
#       the parameter list. Outputs the amount of entries. It creates the lists so the lists do change if the
#       file is opened.
# Preconditions: ip number list and domain name list
# Postconditions: opens the dnstable file with the domain names and ip numbers in them. It uses that
#       information to create a ip number list and a domain name list. it creates the lists so the lists do
#       change. It also outputs the amount of entries
### Design
def gettable(iplst, domainlst):
#  Check to see if dnstable.txt exists, if it doesn't report that it can't open file
    try:
        infile=open("dnstable.txt" , "r")
    except IOError:
        print("Can't open file")
        return

#  read each line of the file
    lst=infile.readlines()
    
#  close the file
    infile.close()

#  report that the dnstable.txt file does exist and is being read.
    print("Reading dnstable.txt")
    

#  for loop that goes through each even line in the lst
    for line in range(0, len(lst)-1, 2):
        
            # a equals the lst of the current line
            a=lst[line]
            
            # b equals the lst after the current line
            b=lst[line+1]
            
            # add the striped version of the line to the domainlst
            domainlst.append(a.strip())
            
            # add the striped version of the line to the iplst
            iplst.append(b.strip())

#  report number of entries on the lists    
    print(len(lst)//2, "entries")
    
######
# Function
# Name: puttable
# Purpose: a function with the job of outputting the contents of the domain name and IP number
#       lists to the dnstable file (overwriting the old data in that file). It will output them in alphabetical
#       order by domain name. It returns nothing. It doesn't change the lists
# Preconditions: domain name list and ip number list
# Postconditions: The function overwrites the old dnstable list with the new domain name list and ip
#       number list assigned to each other. It is presented in alphabetical order.
### Design
def puttable(domainlst, iplst):
#  Open the dnstable file to overwrite only.
    outfile=open("dnstable.txt", "w")
    
#  Run a for loop that goes through the domain name list.
    for i in range(len(domainlst)):
        
        # output domain name and the ip number to the file
        print(domainlst[i], file=outfile)
        print(iplst[i], file=outfile)
        
#  Close the dnstable file.
    outfile.close()
######
# Function
# Name: SET
# Purpose: a function which has the job of setting a domain name / IP number pair, i.e. put the
#           information into the lists. If the domain name is already in the list of domain names, this
#           function should replace the existing IP number associated with the domain name with the
#           new one give from the command. If the domain name is not already in the list of domain
#           names, it and the IP number should be added to the lists. The function should returned the
#           changed lists through the parameters of the function. It changes the lists
# Preconditions:  ip number list, line from command.txt, and the domain name list
# Postconditions: If you do "=" and then a domain name and ip number and the domain name isnt
#           in the domain name list then it adds the domain name and ip number together into the
#           file. If you do "=" and then a domain name and ip number and the domain name is in the
#           domain name list then the ip number you entered replaces the old ip number for the domain name.
## Design
def SET(line, domainlst, iplst):
        # output what is being inserted
        print("Inserting", line[1], line[2])
        
        # if the domain name you entered equals any of the domain names in the domain name list.
        if line[1] in domainlst:
            
                    # the spot in the list equals the spot line[1] is in domainlst
                    spotinlist=domainlst.index(line[1])

                    #   output that the ip number you entered replaces the old ip number thats paired with it
                    print("Found", line[1], "Replacing", iplst[spotinlist], "with", line[2])

                    # the ip number that is paired with the domain name entered equals the ip number in
                    #   requests.txt
                    iplst[spotinlist]=(line[2])
     # else
        else:
                     # add the domain name to the domainlst
                     domainlst.append(line[1])
                     
                     # add the ip number to the iplst
                     iplst.append(line[2])
                     
                     # report that the new entries have been inserted
                     print("New Entry inserted")
                     
        # print the new number of entries
        print("Number of entries now", len(domainlst))
        print()
######
# Function
# Name: GET
# Purpose: A function which has the job of returning a particular domain name, given an IP number,
#           OR returning a particultar IP number, given a domain name. In case of a failed request,
#           "Not found" should be returned. Doesn't change the lists
# Preconditions: the domain name list, line from command.txt, and the ip number list
# Postconditions:Tells you the ip number of a domain name or it
#            tells you the domain name of a ip number. If the domain name or ip number you enter isn't
#            in the file then it prints "Not found". Does not change the lists
## Design
def GET(line, domainlst, iplst):
#  counter equals 0
    GETctr=0
    
#   for loop that goes through the length of the domainlst
    for name in range(len(domainlst)):
        
      # if the ip number is in the line
      if iplst[name] in line:
          
          # counter=1
          GETctr=1
          
          # return the domain name that is paired with the ip number
          return domainlst[name]
        
#    elif domain name is in the line
      elif domainlst[name] in line:
        
          # counter=1
          GETctr=1
          
          # return the ip number that is paired with the domain name
          return iplst[name]
        
#  if the counter equals 1
    if GETctr==0:
        
        # return not found
        return "Not Found"
#
####
# Function
# Name: Show
# Purpose: a function which has the job of displaying to the shell screen, the lists of domain names and
#         IP numbers in alphabetical order. Doesn't change the lists
# Preconditions: the domain name list and the ip number list
# Postconditions: prints out the the domain names and the ip numbers paired together in alphabetical
#         order. Doesn't change the lists
## Design
def SHOW(domainlst, iplst):
#  print a line representing the beginning of the SHOW function
    print("---------------------------------------------")
    
# print out IP Numbers and Domain Names next to each other with a tab inbetween.
    print("IP Numbers \t Domain Names")
    
#  for loop that goes the length of the domainlst
    for name in range(len(domainlst)):
        
        # if the length of the ipnumber is equals 15 or is less than or equal to 9
        if len(iplst[name])==15 or len(iplst[name])<=9:
            
            # print the ip number and domain name with 2 tabs inbetween
            print(iplst[name], "\t\t", domainlst[name])
            
        # else print the ip number and domain name with 1 tab inbetween
        else:   
            print(iplst[name], "\t", domainlst[name])
            
#  print a line representing the end of the SHOW function
    print("---------------------------------------------")
    print()
#
####
# Function
# Name: sort
# Purpose: a function which sorts the two lists according to the values of the domain names,
#       in alphabetical order. The list does change
# Preconditions: The ip number list and the domain name list
# Postconditions: The ip numbers are put together with there assigned domain name. They are then
#       presented in alphabetical order by domain name. the lists are changed in terms of being paired
#       together and in alphabetical order.
# #Design
def sort(iplst, domainlst):
# for loop that goes the length of the domain name list
   for pas in range(len(domainlst)):
       
              # mx equals the max of the domain list minus the pas
              mx=max(domainlst[:len(domainlst)-pas])
              
              # loc_max equals the place of the mas length of mx
              loc_max=domainlst.index(mx)
              
#            replace the domain name of the loc_max with the domain name of the domainlist minus pas
#                   minus 1. Make it so the ip number transfers to the same position on the ip list as the
#                   domain name is on the domain list.
              domainlst[len(domainlst)-pas-1], domainlst[loc_max], iplst[len(domainlst)-pas-1], iplst[loc_max]=domainlst[loc_max], domainlst[len(domainlst)-pas-1], iplst[loc_max], iplst[len(domainlst)-pas-1]
#
#########END OF FUNCTIONS######

    
#  main function design
def main():
    # output introduction message
    print("CS 115 Simulation")

#  domainlst equals an empty list
    domainlst=[]
    
#  iplst equals an empty list
    iplst=[]
    
#   get the lists of domain names and ip numbers, from the dnstable file if it exists and report the
#       dnstable.txt file
    gettable(iplst, domainlst)

#   ask the user for the name of the command file
    print()
    command=input("Name of command file: ")
    print()
    
#   open the file if it exists else report it and end the program
    try:
        cominfile=open(command, "r")
    except IOError:
        print("Can't open command file. Abort program!")
        return
#   read each line of the command file
    comlst=cominfile.readlines()
    
#   for each line in the command file
    for line in comlst:
        
        # split the lines in the command list
        line=line.split()
        
        # call the function that sorts the domain list and ip list  alphabetically
        sort(iplst, domainlst)
        
        # if the command on the line is =
        if line[0]=="=":
            
              # output "Processing SET"
              print("Processing SET")
              
              # send the line to the function that sets a domain name/ip number pair
              SET(line, domainlst, iplst)
              
        # else if the command on the line is ?
        elif line[0]=="?":
            
              # output "Processing GET"
              print("Processing GET")
              
              # send the line to the function that handles a query
              GETresult=GET(line, domainlst, iplst)
              
              # output the result of the query
              print("Lookup of", line[1], "gives", GETresult)
              print()
                  
        # else if the command on the line is *
        elif line[0]=="*":
            
              # output "Processing SHOW"
              print("Processing SHOW")
              
              # call the function that outputs the domain name and ip number lists
              SHOW(domainlst, iplst)
              
        # else report that there is an error with the command you used
        else:
            print("Error in command file", line[0])
            print()
            
#  close the command file 
    cominfile.close()
    
#  call the function that rewrites the dnstable.txt file with the new ip list and domain list.
    puttable(domainlst, iplst)
    
#  put the main()
main()
