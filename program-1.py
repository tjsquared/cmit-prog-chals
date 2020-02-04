# Troy Jasso
# Capital Markets IT Programming Challenge #1

# The challenge is to read weather data from a file,
# compute the temperature spread for each day,
# and then output the day with the minimal temperature spread

# Imports the regex module
import re

# Opens the weather file
print "\nReading weather file...\n"
weatherfile = open("w_data.dat")

# Notes the first lines to read and not read, excluding the header and footer
# For the weather file, the first line to read is line 7,
# and the first line to not read is 37
bodytext = range(7, 37)

# Stores the day of the month and temperature spread for each day
linecount = 1
weatherdata = []
for eachline in weatherfile:
    # Ignores the header and footer lines
    if linecount in bodytext:
        # Removes the special characters from eachline with regex substitution here
        eachline = re.sub('[^A-Za-z0-9 ]+', '', eachline)
        # Splits eachline into columns
        values = eachline.split()
        # Stores the value in column 1 and the difference between columns 2 and 3
        weatherdata.append( [ values[0], float(values[1]) - float(values[2]) ] )
        # Prints the values in columns 1, 2, and 3, and the difference between columns 2 and 3
        print "\tDay: %2s" % values[0], ", High: %5s" % float(values[1]), ", Low: %5s" % float(values[2]), ", Spread: %5s" % ( float(values[1]) - float(values[2]) )

    # Increments the linecount for each line
    linecount = linecount + 1

# Finds the minimum temperature spread
minimaltemperaturespread = weatherdata[0][1]
for eachday in range ( len(weatherdata) ):
    if weatherdata[eachday][1] < minimaltemperaturespread:
        minimaltemperaturespread = weatherdata[eachday][1]

# Finds the day or days with the minimum temperature spread
minimalspreadday = []
for eachday in range ( len(weatherdata) ):
    if weatherdata[eachday][1] == minimaltemperaturespread:
        minimalspreadday.append( weatherdata[eachday][0] )

# Prints the day or days with the minimum temperature spread and the minimum temperature spread
print "\nDay(s) with Minimum Spread: ", minimalspreadday, "; Minimum Spread: ", minimaltemperaturespread, "\n"
