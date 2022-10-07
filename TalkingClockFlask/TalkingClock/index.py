## import modules
import sys

# Objective 1

# Write a command-line program that returns the current time using the "Human Friendly Text" demonstrated in the example below.
# Numeric Time Human Friendly Text

# 1:00 One o'clock
# 2:00 Two o'clock
# 13:00 One o'clock
# 13:05 Five past one
# 13:10 Ten past one
# 13:25 Twenty five past one
# 13:30 Half past one
# 13:35 Twenty five to two
# 13:55 Five to two

# For example, if we execute this program at 16:30, it should output "Half past four"

# $ ..some command..
# Half past four

## step 0, get the command line inputs, and split it apart from the colon:

# TODO make it so that the first letter is capitalised


## TODO a few checks will need to be done here: make sure all hours < 25, make sure mins <60, make
# sure both are >0, make sure there is only 1 ':', does it work with 0's for example 15:01
time_input = sys.argv[1]
hours, minutes = map(int, time_input.split(":"))
## TODO rename array, units doesn't make sense for >10
numbers_units = ["o'clock", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fithteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numbers_tens = ["", "", "twenty", "thirty", "fourty", "fifty"]
quarters = {1: "quarter past ", 2: "half past ", 3: "quarter to "}

def convert_minutes_to_text(number):
    #get the tens
    tens = number // 10
    units = number % 10

    ans = ""

    ## TODO add a space between these
    if number < 20:
        return numbers_units[number]
    if(tens != 0):
        ans += numbers_tens[tens]
    if(units != 0):
        ans += numbers_units[units]
    return ans

def convert_hours_to_text(number):
    ## we want to wrap the 24 hour clock back around to the start of the numbers_units array if it's greater that 12
    if hours < 13:
        return numbers_units[hours]
    else:
        return numbers_units[hours-12]

text_time = ""

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

print(text_time)


