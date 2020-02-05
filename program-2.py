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


# The import command below imports the debugger
# which can be used with the pdb.set_trace command
# to set a breakpoint in the code.
import pdb

# The import command below imports the regex module
# which will be used to remove special characters 
# from our data.
import re

def minimum_spread_finder(filename_to_read,  
        index_column, minuend_column, 
        subtrahend_column):
    """ This function find the minimum spread 
        between two columns of a data file"""

    # The open command below opens the data file.
    print("\nReading", filename_to_read, "file...\n")
    file_to_read = open(filename_to_read)
    
    # The array declared below will store the each index and the spread
    # for each index.
    file_to_read_data = []
    for each_line in file_to_read:
        # The re command below removes the special characters from 
        # each_line with regex substitution.
        each_line = re.sub('[^A-Za-z0-9 ]+', '', each_line)
        # The split command below splits each_line into columns.
        values = each_line.split()
        # The conditional below ignores header and footer lines
        # by checking for number of columns and format.
        if (len(values) >= 3 
                and values[minuend_column - 1].isnumeric() 
                and values[subtrahend_column - 1].isnumeric()):
                # For each line with meaningful data,
                # these commands store the value in the index column 
                # and the difference between the minuend column 
                # and the subtrahend column.
                # The reason for subtracting 1 
                # from the values of the columns 
                # is that the values array is indexed from 0
                # so, e.g., column 1, will have position 0, 
                # column 2 will have position 1, etc.
                # The absolute value is used 
                # to ensure the spread is positive.
                file_to_read_data.append([values[index_column - 1],
                    abs(float(values[minuend_column - 1]) 
                        - float(values[subtrahend_column - 1]))])
                # These lines prints the values in those columns 
                # and the difference.
                print("\tIndex: %15s" % values[index_column - 1],
                        ", Minuend: %5s" 
                        % float(values[minuend_column - 1]),
                        ", Subtrahend: %5s" 
                        % float(values[subtrahend_column - 1]),
                        ", Spread: %5s" 
                        % ( abs( float(values[minuend_column - 1])
                            - float(values[subtrahend_column - 1]))))
    
    # These commands find the minimum spread.
    minimal_spread = file_to_read_data[0][1]
    for each_index in range(len(file_to_read_data)):
        if file_to_read_data[each_index][1] < minimal_spread:
            minimal_spread = file_to_read_data[each_index][1]
    
    # Finds the index or indices with the minimum spread.
    minimal_spreadindex = []
    for each_index in range(len(file_to_read_data)):
        if file_to_read_data[each_index][1] == minimal_spread:
            minimal_spreadindex.append(file_to_read_data[each_index][0])
    
    # Prints the index or indices with the minimum spread and the minimum spread.
    print("\nFile: ", filename_to_read, 
            "; Index (Indices) with Minimum Spread: ", 
            minimal_spreadindex, "; Minimum Spread: ", 
            minimal_spread, "\n")

# These lines call the function with the parameters for the temperature file.
minimum_spread_finder(filename_to_read = "w_data.dat", 
        index_column = 1, minuend_column = 2, 
        subtrahend_column = 3)
# These lines call the function with the parameters for the soccer file.
minimum_spread_finder(filename_to_read = "soccer.dat", 
        index_column = 2, minuend_column = 7, 
        subtrahend_column = 8)

print("Programming Challenge #1 was similar") 
print("to Programming Challenge #2,") 
print("influencing the second program to be more general.\n")
print("The second program calls the same function twice")
print("with different parameters.")
print("The first call finds the spread for the weather data file.")
print("The second call finds the spread for the soccer data file.")
print("Likewise, the same function could be used to find the spread")
print("on a different data file.")
print("The parameters used are filename")
print("and column indicators for the values") 
print("used to calculate the spread.\n")
print ("The minimum spread is returned as a value along with a list of")
print("indices for which it occurs.")
print("Absolute value is used to ensure the spread is positive,")
print("special characters are stripped from each line,")
print("and lines with no relevant data are ignored.\n")
