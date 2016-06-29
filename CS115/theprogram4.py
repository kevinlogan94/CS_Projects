#Prolog  Program 4
# Kevin Logan
# Section 10
# kmlo225@g.uky.edu
# November 15, 2012

#Preconditions:  user inputs:  userid, database filename, search phrase,
#  case sensitivity setting, web page filename

#purpose:
#   search in database file for search phrase, based on case sensitivity
#	setting, and create web page of results (hits or no hits)
#   also keep history of searches in secret.txt

#postcondition: number of hits on the shell, 
#   web page file created with results of search,
#   user name and search phrase appended to secret.txt 

#-----------------------------------------------------
# main function
def main():
#    introductory message
    print("Big Blue Search Engine")
#    input user name, search string, database file name, html file name
#        and case sensitivity
    name=input("Your user name? ")

    database1=input("Enter name of database file  (.txt will be added): ")
    database=database1 + ".txt"

    thekeyword=input("Keyword string to search for: ")

    webpage1=input("Enter name for web page of results  (extension of .htm will be added): ")
    webpage=webpage1 + ".htm"

    case=input("Do you want to be case sensitive?  (y or n) ")


#  try to open database file
#   if cannot open it, 
#     print message and abort program
    try:
        infile= open(database, "r")
    except IOError:
        print("Can't open file")
        return
#  read in the lines from the database file into a 
#      list of strings to search through
#  remember this means first element of list is keyword string, 
#   second element is the URL that goes with the keywords
#   third element more keywords, fourth element is another URL, etc.
#  close input database file
    lst=infile.readlines()
    infile.close()        
#  open output html file
#  prepare it by writing out header
#   output heading on page with search string in it
#  if not case sensitive, force search string to lower case, header says Search for "thekeyword"
    outfile=open(webpage, "w")
    print("<html>", file=outfile)
    print("<title>Search Findings</title>", file=outfile)
    print("<body>", file=outfile)
    if case=="n":
        print("<h2><p align=center>Search for ", '"'+ thekeyword+'"', "</h2>", file=outfile)
        thekeyword=thekeyword.lower()
#   if it is case sensitive than the header says "Case Sensitive Search for "thekeyword"
    else:
        print("<h2><p align=center>Case Sensitive Search for ", '"'+thekeyword+'"', "</h2>", file=outfile)
    
#  initialize hit to zero
    hit=0

#  print that the webpage was created
    print(webpage, "created")

#  for all lines in the list from the database file (hit starts at 0)
    for line in range(0, len(lst)-1, 2):

#       keyword line (call it dbline) is in list at position of line
        dbline=lst[line]
#       URL is at position line + 1
        URL=lst[line+1]
#       if not case sensitive, force the string to lower case
        if case=="n":
            dbline=dbline.lower()

#       if search string is found in dbline
        if dbline.find(thekeyword) >=0:
#            increment hits counter
            hit+=1
#            call function that outputs the hit as line in HTML file
            makehtml(hit, dbline, URL, thekeyword, outfile)

            
#  output # of hits to shell
    print(hit, "hits")
#  if hits is zero
    if hit==0:
#       report failure of search
        print("failure of search")
#       = write "not found" with search phrase to output html file. It displays it in a table in the middle of the screen.
        print("<p align=center>", file=outfile)
        print("<table border>", file=outfile)
        print("<tr><td>", thekeyword, "<td> not found! </tr>", file=outfile)
            
#  output bottom of html page (/table, /body, /html)
#  close output file
    print("</table>", file=outfile)
    print("</body>", file=outfile)
    print("</html>", file=outfile)
    outfile.close()

#  manage the secret file
    thesecret(thekeyword, name)


#-----------------------------------------------------------------

#name  makehtml
#purpose  to output to the html file, the line where the search phrase
#  was found, while bolding every occurrence of that search phrase.
#  It is sure that the phrase is in the line, this function would not be
#  called unless that was true

#preconditions
#    number of hits (the first time a hit is found, the header line of the
#        hit table must be output)
#    the line from the database
#    the URL that goes with the line
#    the search phrase
#    the outputfile object

#postconditions
#    no values returned
#    output html file is altered by the addition of table lines

#design
def makehtml(hit, dbline, URL, thekeyword, outfile):
#    strip the dbline
      dbline=dbline.strip()
#    if first hit,
      if hit==1:
#           make the next thing you put in the html centered
            print("<p align=center>", file=outfile)
#           make a table
            print("<table border>", file=outfile)
#           output the header line of hit table to output file
            print("<tr><th>Hit<th>URL</tr>", file=outfile)
#
#    output the start of the hit table line, <tr><td>
      print("<tr><td>", file=outfile)
#
#    output and replace the the search phrase with <b> and </b> on each side of it.
      print(dbline.replace(thekeyword, "<b>"+thekeyword+"</b>"), file=outfile)


#    output to output file the URL for the link in the second column of the
#	hit table 
            
      print("<td> <a href=", URL, ">", URL, " </a></tr>", sep="", file=outfile)

#------------------------------------------------------------------
#name:  thesecret
#preconditions
#    user name, thekeyword
#
#purpose
#    append to secret file the info username and search phrase
#
#postconditions
#    no return value
#    secret file is altered by writing username and search phrase to it
#
#design
def thesecret(thekeyword, name):
#    open secret file for append
            infile=open("secret.txt", "a")
#    write the person that searched for it
            infile.write(name+"\n")
#    write the search phrase used
            infile.write(thekeyword+"\n")
                  
#    close secret file
            infile.close()
 
main()
