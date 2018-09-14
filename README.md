# divepython2
hello world

12/8/2018 - odd.py - print odd numbers
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

11/8/2018 - first.py - print first programhello world
print "Hello world"

13/8/2018 - positive.py - print positive numbers
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
   
13/8/2018 - zip.py - print zip files
# importing required modules 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "divepython2.zip"
  
# opening the zip file in READ mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file 
    zip.printdir() 
  
    # extracting all the files 
    print('Extracting all the files now...') 
    zip.extractall() 
    print('Done!')
    
13/8/2018 - file.py - print csv
import csv

with open('Popular_Baby_Names.csv','r') as csv_file:
		csv_reader = csv.reader(csv_file)

		for line in csv_reader:
			print(line)
