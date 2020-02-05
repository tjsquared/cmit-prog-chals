# Troy Jasso
# Capital Markets IT Programming Challenge #1

# The challenge is to read weather data from a file,
# compute the temperature spread for each day,
# and then output the day with the minimal temperature spread

# The import statement below imports the debugger.
# It is used with pdb.set_trace() to set breakpoints.
import pdb

# This import statement imports the regex module.
import re

# The open statement below opens the weather data file.
print("\nReading weather file...\n")
weather_file = open("w_data.dat")

# The commands below store the day of the month and temperature spread
# for each day.
weather_data = []
for each_line in weather_file:
    # The re command below removes the special characters from 
    # each_line with regex substitution.
    each_line = re.sub('[^A-Za-z0-9 ]+', '', each_line)
    # The split command below splits each_line into columns.
    values = each_line.split()
    # The conditional below tests by length and format to ignore the header 
    # and footer lines.
    if (len(values) >= 3 
            and values[1].isnumeric() 
            and values[2].isnumeric()):
        # This stores the value in column 1 and the difference between 
        # columns 2 and 3.
        weather_data.append([values[0], 
            float(values[1]) - float(values[2])])
        # This prints the values in columns 1, 2, and 3, and the 
        # difference between columns 2 and 3.
        print("\tDay: %2s" % values[0],
            ", High: %5s" % float(values[1]),
            ", Low: %5s" % float(values[2]),
            ", Spread: %5s" % (float(values[1]) - float(values[2])))

# The commands below find the minimum temperature spread.
minimal_temperature_spread = weather_data[0][1]
for each_day in range(len(weather_data)):
    if weather_data[each_day][1] < minimal_temperature_spread:
        minimal_temperature_spread = weather_data[each_day][1]

# The below commands find the day or days with the minimum temperature spread.
minimal_spread_day = []
for each_day in range(len(weather_data)):
    if weather_data[each_day][1] == minimal_temperature_spread:
        minimal_spread_day.append(weather_data[each_day][0])

# The below command prints the day or days with the minimum temperature
# spread and the minimum temperature spread.
print ("\nDay(s) with Minimum Spread: ", minimal_spread_day, 
        "; Minimum Spread: ", minimal_temperature_spread, "\n")
