import sgp4
from sgp4.earth_gravity import wgs72  # this is the General Earth Calcuation
from sgp4.io import twoline2rv
from datetime import datetime
import time
from czml import czml
from urllib import request
import requests  # importing the request module to get from the web

# Will be used to write in the cartesian
# def write_cartesian():
#    pass
# Will be used to write in the position
# def write_positions():
#    pass
# will be used to write in the files


# def write_to_file(filename='example.czml',data=''):
#     doc = czml.CZML() # Creates the czml for the specified document .
#     packet1 = czml.CZMLPacket(id='document',version = '0.1')  # Adding in the czml format and the version

'''Sample Checking of the sgp4 '''

# Taking the date input
'''# UNCOMMENT THESE BELOW LINES AFTER YOU ARE DONE'''
# date_input_from = input("Enter the date you want to propage from in the format of : YYYY MM DD HH MM SS :")
# date_input = input("Enter the date you want to propogate to in the format of : YYYY MM DD HH MM SS :")
date_input_from = "2016 10 30 00 00 00"
date_input = "2016 10 31 00 00 00"
date_list = date_input.strip().split(" ")
date_list_from = date_input_from.strip().split(" ")
# Initializing all the date parameters
date_year, date_month, date_day, date_hour, date_minute, date_second = date_list
date_from_year, date_from_month, date_from_day, date_from_hour, date_from_minute, date_from_second = date_list_from
# Converting all the desired stuff in the form of an integer to get the specified Values .
date_year, date_month, date_day, date_hour, date_minute, date_second = int(date_year), int(date_month), int(
    date_day), int(date_hour), int(date_minute), int(date_second)
date_from_year, date_from_month, date_from_day, date_from_hour, date_from_minute, date_from_second = int(
    date_from_year), int(date_from_month), int(date_from_day), int(date_from_hour), int(date_from_minute), int(
    date_from_second)
# exit(0)

# Getting the linear distance from the web
# hdr = {
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
#         'Accept-Encoding': 'none',
#         'Accept-Language': 'en-US,en;q=0.8',
#         'Connection': 'keep-alive'}  # this is the main header which will be passed to a website.

# Below is the call to the specified Function
# web_check = requests.get("https://www.celestrak.com/cgi-bin/TLE.pl?CATNR=25544", headers=hdr,verify=False) # This reads the urlpage
# urllib.request.get("https://www.celestrak.com/cgi-bin/TLE.pl?CATNR=25544", headers=hdr,verify=False)
# session.get("https://www.celestrak.com/cgi-bin/TLE.pl?CATNR=25544", headers=hdr,verify=False)
# THE ABOVE BOTH ARE NOT WORKING , STILL
# print(web_check)
# #print(web_check)
# exit(0) Debugging !
# Specifying the two line ranges
line1 = ('1 00005U 58002B   00179.78495062  .00000023  00000-0  28098-4 0  4753')  # Linear1
line2 = ('2 00005  34.2682 348.7242 1859667 331.7664  19.3264 10.82419157413667')  # Linear2
satellite = twoline2rv(line1, line2, wgs72)  # Retrieves the position of the satelites with all the other properties
# DEBUGGING PURPOSE
print("*" * 50)
print("Propagating TO : ")
print("Year : ", date_year)
print("Month: ", date_month)
print("Day : ", date_day)
print("Hour: ", date_hour)
print("Minutes: ", date_minute)
print("Seconds:  ", date_second)
print("*" * 50)
print("propagating from")
print("Year : ", date_from_year)
print("Month: ", date_from_month)
print("Day : ", date_from_day)
print("Hour: ", date_from_hour)
print("Minutes: ", date_from_minute)
print("Seconds:  ", date_from_second)
print("*" * 50)
# exit(0) # DEBUGGING
# HERE YOU NEED TO SPECIFY THE TIME RANGE LOOP , AFTER 300 SECONDS IT WILL KEEP ON CHANGING #
# Converting the Time to the seconds format !
# dt_from = datetime(date_from_year,date_from_month,date_from_day,date_from_hour,date_from_minute, date_from_second)
# dt_from_s = time.mktime(dt_from.timetuple()) # Gets the seconds in the from list

Ending_seconds_timestamp = time.mktime(
    datetime(date_year, date_month, date_day, date_hour, date_minute, date_second).timetuple())
starting_seconds_timestamp = time.mktime(
    datetime(date_from_year, date_from_month, date_from_day, date_from_hour, date_from_minute,
             date_from_second).timetuple())  # Gets the Seconds from the TO LIST (DATE)
interval = None  # This interval should be based onthe time Interval  !
print("Starting Seconds : ", starting_seconds_timestamp)  # DEBUGGING
print("Ending Seconds : ", Ending_seconds_timestamp)  # DEBUGGING
print("TOTAL RANGE OF SECONDS", (int(Ending_seconds_timestamp) - int(starting_seconds_timestamp)))
if Ending_seconds_timestamp < starting_seconds_timestamp:  # CHECK CONDITION , IF YOU WANT _VE PROPAGATION WILL WORK ON LATER (IF REQUIRED)
    print("Possible You are propagating Back, right now its for Forward ")
    exit(0)
current_second = 0  # KEEP THE TRACK OF THE SECONDS PASSED.
cartesian_list = []  # This list will hold all the vectors !
velocity_position_list = []  # Velocity at a specified position , mentioning !
total_interval_length = len(range(int(starting_seconds_timestamp), int(Ending_seconds_timestamp), 300))
counter = 0  # This is for checking in the Partial time , the last rest which will be covered in the last

check = 0  # This is for the Conditional Check
# If the Modulus of 300 is == 0, then you don't need the last Partial interval calculation !
if (int(Ending_seconds_timestamp) - int(starting_seconds_timestamp)) % 300 != 0:
    check = 1  # This will check
print(total_interval_length)  # Debugging !!!!
# exit(0) # Exits the program
Total_number_of_orbits = int((int(Ending_seconds_timestamp) - int(starting_seconds_timestamp)) / 6098)
# The above are the total Number of Orbits Which will be discovered
# if type(Total_number_of_orbits) == int:
#     Total_number_of_orbits = Total_number_of_orbits
# elif type(Total_number_of_orbits) == float:
#     Partial_number_of_orbits = int(str(Total_number_of_orbits).split('.')[1])
#     Total_number_of_orbits = int(Total_number_of_orbits)
# exit(0)
Partial_orbit = (int(Ending_seconds_timestamp) - int(starting_seconds_timestamp)) - (Total_number_of_orbits * (6078))
print("Total Number of Orbits (Complete) [/ 6078 --> ]: ",
      Total_number_of_orbits)  # Printing the total number of orbits !
print("Partial Orbit is Seconds:(Partial ) : ", Partial_orbit)  # Partial Orbit printing
trail_time_list = []  # Trail time dictionary !
lead_time_list = []
counter = 0
previous_trailing_time = None  # This is the variabe to keep the track of the trailing time
for _ in range(int(starting_seconds_timestamp), int(Ending_seconds_timestamp),
               6078):  # These will be the complete orbits  !
    if counter == 0:
        start_trail_time = datetime.fromtimestamp(
            int(starting_seconds_timestamp))  # Gets the first timestamp for the stuff
        epoch_time = start_trail_time
        next_time_interval = datetime.fromtimestamp(
            int(starting_seconds_timestamp) + 6078)  # This adds up the next time stamp , after
        interval = str(epoch_time) + "//\\" + str(next_time_interval)
        current_dict = {"epoch": str(epoch_time), "interval": interval,
                        "number": [0, 0, 6078.0997363701, 6078.0997363701]}  # This Creates the specified dictionary
        lead_cur_dict = {"epoch": str(epoch_time), "interval": interval,
                         "number": [0, 6078.0997363701, 6078.0997363701, 0]}
        trail_time_list.append(current_dict)  # Adds up the current dictionary in the interval.!
        lead_time_list.append(lead_cur_dict)  # Adds the dictionary to the lead current dictionary !
        previous_trailing_time = datetime.fromtimestamp(
            int(starting_seconds_timestamp) + 6078)  # Conversion of the Date time to the specified module !
        # print(start_trail_time)
        # print("EPOCH TIME :",epoch_time)
        # print("NEXT TIME : ",next_time_interval)
        # print("INTERVAL :",interval)
        # print("Previous trailing time : ",previous_trailing_time)
        print("Trailing TIME: ", current_dict)
        print("Lead Time : ", lead_cur_dict)
        counter += 1
        # exit()
    else:
        if counter < Total_number_of_orbits:
            start_trail_time = previous_trailing_time
            epoch_time = start_trail_time
            next_time_interval = datetime.fromtimestamp(int(_) + 6078)  # This adds up the next time stamp.
            interval = str(epoch_time) + "//\\" + str(next_time_interval)
            current_dict = {"epoch": str(epoch_time), "interval": interval,
                            "number": [0, 0, 6078.0997363701, 6078.0997363701]}  # This Creates the specified dictionary
            lead_cur_dict = {"epoch": str(epoch_time), "interval": interval,
                             "number": [0, 6078.0997363701, 6078.0997363701, 0]}
            trail_time_list.append(current_dict)
            lead_time_list.append(lead_cur_dict)  # Adds the dictionary to the lead current dictionary !
            # print("EPOCH TIME :", epoch_time)
            # print("NEXT TIME : ", next_time_interval)
            # print("INTERVAL :", interval)
            # print("Previous trailing time : ", previous_trailing_time)
            print("Trailing TIME: ", current_dict)  # CURRENT TRAILING TIME
            print("Lead Time dict : ", lead_cur_dict)  # LEAD TRAILING TIME
            previous_trailing_time = next_time_interval
            counter += 1
        elif counter == Total_number_of_orbits:
            start_trail_time = previous_trailing_time  # This will hold the previous value for the trail time  !
            epoch_time = start_trail_time
            next_time_interval = datetime.fromtimestamp(Ending_seconds_timestamp)
            interval = str(epoch_time) + "//\\" + str(next_time_interval)
            current_dict = {"epoch": str(epoch_time), "interval": interval,
                            "number": [0, 0, 6078.0997363701, 6078.0997363701]}  # This Creates the specified dictionary
            lead_cur_dict = {"epoch": str(epoch_time), "interval": interval,
                             "number": [0, 6078.0997363701, 6078.0997363701, 0]}
            trail_time_list.append(current_dict)
            lead_time_list.append(lead_cur_dict)  # Adds the dictionary to the lead current dictionary !
            print("Trailing TIME: ", current_dict)  # CURRENT TRAILING TIME
            print("Lead Time dict : ", lead_cur_dict)  # LEAD TRAILING TIME
            counter += 1
# COUNTING IN THE PARTIAL ORBIT STUFF, SO THAT IT MAY BE ADDED IN THE TRAILING AND THE LEADING FORMAT !
ending_trail_time = Partial_orbit  # This gets the seconds of the specified orbit which is partial  !!

counter = 0
# Satellite propagation , for the specified velocities and the positions
''' ---- THE BELOW WORKSPACE, is for the position , the above one is for the lead and the trail time ! '''
for _ in range(int(starting_seconds_timestamp), int(Ending_seconds_timestamp), 300):
    # print("Current Second :", current_second)
    current_time = datetime.fromtimestamp(_)  # Gets back the time stamp in the form of all the stuff
    starting_time = current_time  # This will be used later for calculating orbits. !
    epoch_time = datetime.fromtimestamp(_)  # This is the EPOCH interval starting time
    # print("Epoch TIME INTERVAL : ", epoch_time)
    # Position
    position, velocity = satellite.propagate(current_time.year, current_time.month, current_time.second,
                                             current_time.hour, current_time.minute,
                                             current_time.second)  # Gets the position and the velocity at the specified place
    # SECOND!!!!
    cartesian_list.append(current_second)  # This appends the current second
    velocity_position_list.append(current_second)
    # VECTOR !!!!!!
    # Inserting in all the axis in the List of the position !

    for single_axis in position:  # looping through each of the position !
        cartesian_list.append(single_axis)  # Adds in the single axis position
    for velocity_direction in velocity:
        velocity_position_list.append(velocity_direction)  # Appends in the velocity of the direction ! !

    # print(satellite.error) # If there is an error , non zero error are displayed here
    # print(satellite.error_message) # Prints the error message in case of the error
    # print("The lenght of the specified attributes were : \n")
    # print(len(position)) # prints out the number of position in the position element
    # print(len(velocity)) # Prints out the number of velocities it did changed!
    # print("The Values are : ")
    # print(position.cartesian())
    # print("POSITION : ", position)  # Kilometer from the center of earth
    # print("VELOCITY : ", velocity)  # KM / S (kilometer per second)
    # if counter == 0 :
    #    trail_time_dict["epoch"] = epoch_time # this inserts into the epoch time !
    current_second += 300
    counter += 1  # Increments it b
    if check == 1:
        if counter == total_interval_length:  # Looping to the last element of the stuff, because if the value not % 300
            # print("Ending timestamp :", Ending_seconds_timestamp) Debugging !
            # print("Right now time :",starting_seconds_timestamp )
            seconds_left = Ending_seconds_timestamp - (starting_seconds_timestamp + current_second)
            unresolved_sec = _ + seconds_left  # This Creates up the ending seconds of the stuff
            # print("SECONDS LEFT :", seconds_left)
            # print("unresolved sec: ",unresolved_sec )
            ##print(unresolved_sec)
            current_time = datetime.fromtimestamp(
                unresolved_sec)  # Gets back the time stamp in the form of all the stuff
            position, velocity = satellite.propagate(current_time.year, current_time.month, current_time.second,
                                                     current_time.hour, current_time.minute,
                                                     current_time.second)  # Gets the position and the velocity at the specified place
            cartesian_list.append(current_second + seconds_left)  # This appends the current second
            print(current_second + seconds_left)
            velocity_position_list.append(current_second + seconds_left)
            epoch_time = datetime.fromtimestamp(
                starting_seconds_timestamp + current_second + seconds_left)  # This is the EPOCH interval starting time
            print("Epoch TIME INTERVAL : ", epoch_time)
            # print("Last time interval : ", current_second + seconds_left)
            # VECTOR !!!!!!
            # Inserting in all the axis in the List of the position !
            for single_axis in position:  # looping through each of the position !
                cartesian_list.append(single_axis)  # Adds in the single axis position
            for axis_velocity in velocity:
                velocity_position_list.append(axis_velocity)  # Adds in the axis velocity as well
                # DO SOME THING HERE
    elif counter == total_interval_length:
        epoch_time = datetime.fromtimestamp(_)  # This is the EPOCH interval starting time
        # print("Epoch TIME INTERVAL : ", epoch_time)
        # Position
        position, velocity = satellite.propagate(current_time.year, current_time.month, current_time.second,
                                                 current_time.hour, current_time.minute,
                                                 current_time.second)  # Gets the position and the velocity at the specified place
        # SECOND!!!!
        cartesian_list.append(current_second)  # This appends the current second
        velocity_position_list.append(current_second)
        # VECTOR !!!!!!
        # Inserting in all the axis in the List of the position !

        for single_axis in position:  # looping through each of the position !
            cartesian_list.append(single_axis)  # Adds in the single axis position
        for velocity_direction in velocity:
            velocity_position_list.append(velocity_direction)  # Appends in the velocity of the direction ! !
            # pass # HERE ADD IF THE CHECK != 1 and other things
print("CATERSIAN POSITION : SECONDS, X-AXIS , Y-AXIS, Z-AXIS, REPEAT!! ...")
print(
    cartesian_list)  # Debugging purpose , gets all the Cartesian_list , which will be used as a dictionary in the json file creation !
print("VELOCITY AT SECONDS, XAXIS, Y AXIS, Z AXIS")
print(velocity_position_list)
