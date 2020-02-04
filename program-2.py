# Troy Jasso
# Capital Markets IT Programming Challenge #2

# The challenge is to read soccer data from a file,
# compute the goal spread for each team,
# and then output the team with the minimal goal spread.
# Additionally, we should state the influence 
# of Programming Challenge #1 on Programming Challenge #2.
# We do that here.
# The Programming Challenges #1 and #2 are the same
# from an abstract point of view.
# Therefore, for Programming Challenge #2, we write
# a more general program which can output
# the result for either programming challenge
# depending on the parameters of the output function.


# Imports the debugger
import pdb

# Imports the regex module
import re

def MinimumSpreadFinder(filenametoread, firstlinetoread, firstlinenottoread, indexcolumn, minuendcolumn, subtrahendcolumn):

    # Opens the soccer file
    print "\nReading", filenametoread, "file...\n"
    filetoread = open(filenametoread)
    
    # Notes the first lines to read and not read, excluding the header and footer
    bodytext = range(firstlinetoread, firstlinenottoread)
    
    # Stores the index of the month and  spread for each index
    linecount = 1
    filetoreaddata = []
    for eachline in filetoread:
        # Ignores the header and footer lines
        if linecount in bodytext:
            # Removes the special characters from eachline with regex substitution here
            eachline = re.sub('[^A-Za-z0-9 ]+', '', eachline)
            # Splits eachline into columns
            values = eachline.split()
            # For each line with meaningful data
            if len(values) > 0:
                # Stores the value in the index column and the difference between the minuend column and the subtrahend column
                # The reason for subtracting one from the values of the columns is that the values array is indexed from 0
                # so, e.g., column 1, will have position 0, column 2 will have position 1, etc.
                # The absolute value is used since to ensure the spread is positive
                filetoreaddata.append( [ values[indexcolumn - 1], abs(float(values[minuendcolumn - 1]) - float(values[subtrahendcolumn - 1])) ] )
                # Prints the values in those columns and the difference
                print "\tIndex: %15s" % values[indexcolumn - 1], ", Minuend: %5s" % float(values[minuendcolumn - 1]), ", Subtrahend: %5s" % float(values[subtrahendcolumn - 1]), ", Spread: %5s" % ( abs( float(values[minuendcolumn - 1]) - float(values[subtrahendcolumn - 1]) ) )
    
        # Increments the linecount for each line
        linecount = linecount + 1
    
    # Finds the minimum spread
    minimalspread = filetoreaddata[0][1]
    for eachindex in range ( len(filetoreaddata) ):
        if filetoreaddata[eachindex][1] < minimalspread:
            minimalspread = filetoreaddata[eachindex][1]
    
    # Finds the index or indexs with the minimum  spread
    minimalspreadindex = []
    for eachindex in range ( len(filetoreaddata) ):
        if filetoreaddata[eachindex][1] == minimalspread:
            minimalspreadindex.append( filetoreaddata[eachindex][0] )
    
    # Prints the index or indexs with the minimum  spread and the minimum  spread
    print "\nFile: ", filenametoread, "; Index (Indices) with Minimum Spread: ", minimalspreadindex, "; Minimum Spread: ", minimalspread, "\n"

# Calls the function with the parameters for the temperature file
MinimumSpreadFinder(filenametoread = "w_data.dat", firstlinetoread = 7, firstlinenottoread = 37, indexcolumn = 1, minuendcolumn = 2, subtrahendcolumn = 3)
# Calls the function with the parameters for the soccer file
MinimumSpreadFinder(filenametoread = "soccer.dat", firstlinetoread = 4, firstlinenottoread = 25, indexcolumn = 2, minuendcolumn = 7, subtrahendcolumn = 8)

print "Programming Challenge #1 was similar to Programming Challenge #2, influencing the second program to be more general."
print "The second program calls the same function twice with different parameters."
print "The first call finds the spread for the weather data file."
print "The second call finds the spread for the soccer data file."
print "Likewise, the same function could be used to find the spread on a different data file."
print "The parameters used are filename, header and footer line indicators, and column indicators for the values used to calculate the spread."
print "The minimum spread is returned as a value along with a list of indices for which it occurs."
print "Absolute value is used to ensure the spread is positive, special characters are stripped from each line, and lines with no relevant data are ignored.\n"

