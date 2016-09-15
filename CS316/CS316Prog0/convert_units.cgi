#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb, os

# Function for Form Validation
# Return Value: True = Valid information was submitted
#		False = Invalid information was submitted 
def formValidation(number, unit, new_unit):
     unit_types = ['kilometers', 'meters', 'miles', 'feet', 'celsius', 'fahrenheit', 'kelvin', 'hours', 'minutes', 'seconds', 'days']
     new_unit_ctr = 0
     unit_ctr = 0
     try:
      #Check if the user inputted anything
      if ((number == None) or (unit == None) or (new_unit == None)):
       raise ValueError
      else:
       #Check if the conversion units are in our types for the program
       for unit_type in unit_types:
         if (unit_type == unit):
           unit_ctr += 1
         if (unit_type == new_unit):
           new_unit_ctr += 1
       if ((unit_ctr == 0) or (new_unit_ctr == 0)):
	 raise ValueError
  
      #Check if number is an integer/float and if it's negative.
      if (float(number) < 0):
        raise ValueError
      return True
     except ValueError:
      print "<h1>Error</h1>"
      print "<h2>Please input valid Information!!</h2>"
      print "<p>Negative numbers aren't allowed in this program.\n</p>"
      print "<p><b>Allowed Conversion Units:</b></p>"
      print "<p>Measurement: Meters, Kilometers, Miles, Feet</p>"
      print "<p>Temperature: Kelvin, Fahrenheit, Celsius</p>"
      print "<p>Time: Days, Hours, Seconds, Minutes</p>"
      return False


# Function to process the conversion then print to the screen
# 	Conversion: Measurement: Meters, Kilometers, Miles, Feet
#		    Temperature: Kelvin, Fahrenheit, Celsius
#		    Time: Days, Hours, Seconds, Minutes
def convertion(number, unit, new_unit):
   number = float(number)
   #Measurement Conversion
   if (unit == 'meters') and (new_unit == 'kilometers'):
	new_number = (number * .001)
   elif (unit == 'meters') and (new_unit == 'feet'):
        new_number = (number * 3.28084)
   elif (unit == 'meters') and (new_unit == 'miles'):
        new_number = (number * 0.00062137)
   elif (unit == 'kilometers') and (new_unit == 'meters'):
        new_number = (number * 1000)
   elif (unit == 'kilometers') and (new_unit == 'feet'):
        new_number = (number * 3280.84)
   elif (unit == 'kilometers') and (new_unit == 'miles'):
        new_number = (number * 0.62137)
   elif (unit == 'miles') and (new_unit == 'kilometers'):
        new_number = (number / 0.62137)
   elif (unit == 'miles') and (new_unit == 'meters'):
        new_number = (number / 0.00062137)
   elif (unit == 'miles') and (new_unit == 'feet'):
        new_number = (number * 5280)
   elif (unit == 'feet') and (new_unit == 'meters'):
        new_number = (number / 3.28084)
   elif (unit == 'feet') and (new_unit == 'miles'):
        new_number = (number / 5280)
   elif (unit == 'feet') and (new_unit == 'kilometers'):
        new_number = (number / 3280.84)
   #Temperature Conversion
   elif (unit == 'celsius') and (new_unit == 'kelvin'):
        new_number = (number + 273.15)
   elif (unit == 'celsius') and (new_unit == 'fahrenheit'):
        new_number = (number * 1.8 + 32)
   elif (unit == 'fahrenheit') and (new_unit == 'celsius'):
        new_number = (number - 32 / 1.8)
   elif (unit == 'fahrenheit') and (new_unit == 'kelvin'):
        new_number = ((number + 459.67) * 5/9)
   elif (unit == 'kelvin') and (new_unit == 'celsius'):
        new_number = (number - 273.15)
   elif (unit == 'kelvin') and (new_unit == 'fahrenheit'):
        new_number = (number * 9/5 - 459.67)
   #Time Conversion
   elif (unit == 'hours') and (new_unit == 'minutes'):
        new_number = (number * 60)
   elif (unit == 'hours') and (new_unit == 'seconds'):
	new_number = (number * 3600)
   elif (unit == 'hours') and (new_unit == 'days'):
        new_number = (number / 24)
   elif (unit == 'minutes') and (new_unit == 'days'):
        new_number = (number / 1440)
   elif (unit == 'minutes') and (new_unit == 'seconds'):
        new_number = (number * 60)
   elif (unit == 'minutes') and (new_unit == 'hours'):
        new_number = (number / 60)
   elif (unit == 'days') and (new_unit == 'minutes'):
        new_number = (number * 1440)
   elif (unit == 'days') and (new_unit == 'seconds'):
        new_number = (number * 86400)
   elif (unit == 'days') and (new_unit == 'hours'):
        new_number = (number * 24)
   elif (unit == 'seconds') and (new_unit == 'hours'):
        new_number = (number / 3600)
   elif (unit == 'seconds') and (new_unit == 'days'):
        new_number = (number / 86400)
   elif (unit == 'seconds') and (new_unit == 'minutes'):
        new_number = (number / 60)
   #If conversion is to the same unit
   elif (unit == new_unit):
        new_number = number
   #Otherwise it can't be converted
   else:
        print "<h1>Error</h1>"
        print "<h2>Convertion from %s to %s isn't possible.</h2>" % (unit, new_unit)
        return

   print "<h2>Measurement Input: %s %s</h2>" % (number, unit)
   print "<h2>Result: %s %s </h2>" % (new_number, new_unit)
   return


def main():
 #Set up CGI page
 print "Content-type:text/html\r\n\r\n"
 print "<html>"
 print "<head>"
 print "<title>CS316 Program 0</title>"
 print "</head>"
 print "<body>"
 print "<h1>Python Measurement Conversion</h1>"
 
 #Check if a GET request is being sent
 if (os.environ['REQUEST_METHOD'] == 'GET'):
  # Create instance of FieldStorage 
  form = cgi.FieldStorage()

  # Get data from fields. Make strings lowercase
  number = form.getvalue('number')
  unit = form.getvalue('unit')
  new_unit = form.getvalue('new_unit')

  #If unit or new_unit isn't None make them lowercase.
  if (unit != None):
   unit = unit.lower()
  if (new_unit != None):
   new_unit = new_unit.lower()
 
  #Check if form validation passes, if so then run conversion
  form_pass = formValidation(number, unit, new_unit)
  if (form_pass == True):
   convertion(number, unit, new_unit)
  print "</body>"
  print "</html>"
 #If not a GET request, report Error
 else:
  print "<h2>Wrong Request was sent</h2>"
  print "Request Type: %s" % (os.environ['REQUEST_METHOD'])
  print "</body>"
  print "</html>"

#call the main
main()
