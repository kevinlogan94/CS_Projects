#Lab 13
#Kevin Logan
#Section 10
#November 8, 2012

def main():
   mydata = input("Filename? ")
   try:
     infile  = open(mydata, "r")
   except IOError:
     print("Can't open file")
     return

   ctr = 0
   total= 0
   for line in infile.readlines():
     avg = process(line)
     total += avg
     print(avg)
     ctr +=1
   print("\nAverage over all students =", end=" ")
   if total > 0:
      print(total / ctr)
   else:
      print(0)
     
   infile.close()

def process (line):
   lst = line.split()
   #  first name, last name, 5 grades
   tot = 0
   print(lst[0], lst[1], end=" ")
   for i in range(2, len(lst)):
      gr = float(lst[i])
      tot += gr
   return tot/5
      
main()
