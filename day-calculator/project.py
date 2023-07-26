hours = int(24)
minutes = int(60*hours)

def days_of_units(day, unit):
            day_input = int(day)
            unit_input = str(unit)
            if unit_input == "hours":
                return f"{day_input} days equal to { day_input * hours} Hours\n"
            elif unit_input == "minutes":
                return f"{day_input} days equal to { day_input * minutes} Minutes\n"
            
def day_validate(day):
    try:
        day_input = int(day)
        if day_input < 0:
            exit("Please enter a Positive day number :)")
        elif day_input >=0 :
            return ""
    except ValueError:
        exit("Your input is not a number ")
    
def unit_validate(unit):
    try:
        unit_input = str(unit)
        if unit_input == "hours" :
            return ""
        elif unit_input == "minutes":
            return ""
        else : 
            exit("Please select one of option units curently :)")
    except ValueError:
            exit("Your input is not a string ")

while True:
    days = input("Enter the number of days you want to convert : (Enter 'q' to exit) ")
    if days == "q":
        exit("Goodbye")
    print(day_validate(days))

    units = input("Convert to hours and minutes? ")
    print(unit_validate(units))

    resulte = days_of_units(days, units)
    print(resulte)
