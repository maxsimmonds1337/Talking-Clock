## import modules
import sys
from time import localtime, strftime 

## TODO make sure there is only 1 ':', make sure non numerics are handled well
numbers_units = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fithteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers_tens = ["", "", "twenty", "thirty", "fourty", "fifty"]
quarters = {1: "quarter past ", 2: "half past ", 3: "quarter to "}
hours = 0
minutes = 0

def convert_minutes_to_text(number):
    ans = ""
    tens = number // 10
    units = number % 10

    if number < 20:
        return numbers_units[number]
    if(tens != 0):
        ans += numbers_tens[tens]
    if(units != 0):
        if ans != "":
            ans += " "  ## add a space if ans is not empty, prevents whitespace at end
        ans += numbers_units[units]
    return ans

def convert_hours_to_text(number):
    ## we want to wrap the 24 hour clock back around to the start of the numbers_units array if it's greater that 12
    if number < 13:
        return numbers_units[number]
    else:
        return numbers_units[number-12]

def TalkingClock():

    text_time = ""
    number_of_args = len(sys.argv)

    # check to see if there are too many args, or if the user wants the current time, or to request a time
    if number_of_args > 2:
        exit("\nusage: TalkingClock.py [HH:MM]\n")
    elif number_of_args == 1:
        time_input = strftime("%H:%M", localtime()) ## get the local time from the PC
    else:
        time_input = sys.argv[1]

    hours, minutes = map(int, time_input.split(":"))

    # check to make sure the input is correct (non negative and hours < 24, mins <60)
    if (hours > 23) or (minutes > 59) or (hours < 0) or (minutes < 0):
        exit("\nusage: TalkingClock.py [HH:MM]\n")

    if minutes == 0:
        ## if there are no minutes, then it's an "o'clock" at the end, this is handled neatly by the 0 index of the numbers_units array
        text_time += convert_hours_to_text(hours)
        text_time += " "
        text_time += convert_minutes_to_text(minutes)

    elif minutes % 15 == 0:
        #if we're here, then minutes is either 15, 30, or 45 (can't be zero, as the case above catches that)
        quarters_index = minutes//15
        text_time += quarters[quarters_index]
        if quarters_index == 3:
            # if it's 3, then we're "quarter to" which means the hour needs to be incremented
            hours+=1
        text_time += convert_hours_to_text(hours)

    elif(minutes > 30):
        hours += 1  ## if we're here, then we need to say were 'x' _to_ the up and coming hour, so inc the hour
        text_time += convert_minutes_to_text(60-minutes)    ## subtract 30, so we correctly say the number of minutes left until the next hour
        text_time += " to " ## if we're greater than 30 mins, we say "to" the next hour
        text_time += convert_hours_to_text(hours)
    else:
        ## if not, then we're 'x' minutes "past" the current hour
        text_time += convert_minutes_to_text(minutes)   
        text_time += " past "
        text_time += convert_hours_to_text(hours)

    return text_time.capitalize()  ## make the first letter a captial


##ask if this is okay to do?
if __name__ != '__main__':
    TalkingClock()  # next section explains the use of sys.exit
else:
    print(TalkingClock())