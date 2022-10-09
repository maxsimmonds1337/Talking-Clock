# content of test_sample.py
from TalkingClock import *

def test_answer():
    # if convert_minutes_to_text(20) == "twenty":
    #     print("yes")
    # else:
    #     print("no {0}".format(convert_minutes_to_text(20)))
    assert convert_minutes_to_text(20) == 'twenty'
    assert convert_hours_to_text(10) == 'ten'
