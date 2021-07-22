"""
 Convert the Nordics CSV File.
 Remove the return cariage issue in the "New Event" field
 (If not a ligne is displayed in two lines in Excel)
"""
import re
import csv

REGEX = r"New Event:\nhttps:[-a-zA-Z0-9/._?=&]*"
SUBST = ""
ORIGINALNORDICSFILENAME = "original_nordics.csv"
FINALNORDICS = "final_nordics.csv"
test_str = ""

file = open(ORIGINALNORDICSFILENAME)
test_str = file.read()
file.close()
# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(REGEX, SUBST, test_str, 0, re.MULTILINE)

if result:
    print (result)
    file = open(FINALNORDICS, "wt")
    test_str = file.write(result)
    file.close()

print("Nordics file is converted")