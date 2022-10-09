# content of test_sample.py
from TalkingClock import convert_minutes_to_text

def test_answer():
    # if convert_minutes_to_text(20) == "twenty":
    #     print("yes")
    # else:
    #     print("no {0}".format(convert_minutes_to_text(20)))
    assert convert_minutes_to_text(20) == 'twenty'
