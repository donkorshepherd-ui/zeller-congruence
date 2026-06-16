# File: zeller.py
# Description: Calculate day of week using Zeller's Congruence
#Assignment Number: 5
#Name: DONKOR SHEPHERD MENSAH
#SID: 2425404178
#Email: donkorshepherd1@gmail.com
#Grader: Carolyn
# on my honor, DONKOR SHEPHERD MENSAH, this programming assignment is my own work
#and I have not provided this code to any other student.

# 1. Get input
month_name = input("please enter your month_name (for example, January, February, etc.): ")
day = int(input("please enter your day (an integer): "))
year = int(input("please enter your year (an integer): "))

# Convert month name to month_number
# Jan=13,  Feb=14,  March=3, ..... Dec=12
if month_name == "January":
    month_number = 13
    year = year - 1
elif month_name == "February":
    month_number = 14
    year = year - 1
elif month_name == "March":
    month_number = 3
elif month_name == "April":
    month_number = 4
elif month_name == "May":
    month_number = 5
elif month_name == "June":
    month_number = 6
elif month_name == "July":
    month_number = 7
elif month_name == "August":
    month_number = 8
elif month_name == "September":
    month_number = 9
elif month_name == "October":
    month_number = 10
elif month_name == "November":
    month_number = 11
else:  # December
    month_number = 12

    # 2 Set variables as per algorithm
    day_in_month = day
    year_in_century = year % 100
    century = year // 100

 # 4. calculate quantities
    variation_in_days_per_month = (13 * (month_number + 1)) // 5
    leap_year_days = year_in_century // 4
    century_days = century // 4

# 5. Total days and day of week
    total_days = day_in_month + variation_in_days_per_month + year_in_century + leap_year_days + century_days + 5 * century
    day_of_week = total_days % 7

# 6. Convert to day name
if day_of_week == 0:
    day_name= "Saturday"
elif day_of_week == 1:
    day_name = "Sunday"
elif day_of_week == 2:
    day_name = "Monday"
elif day_of_week == 3:
    day_name = "Tuesday"
elif day_of_week == 4:
    day_name = "Wednesday"
elif day_of_week == 5:
    day_name = "Thursday"
else: # this means day_of_week == 6
    day_name = "Friday"

# 7. print exactly as required
print("The day of the week is", day_name + "." )
