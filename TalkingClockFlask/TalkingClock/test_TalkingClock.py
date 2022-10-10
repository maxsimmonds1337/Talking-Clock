# content of test_sample.py
from TalkingClock import *
import pytest
from time import localtime, strftime 

@pytest.mark.parametrize("test_minutes,expected", [(20,"twenty"), (10, "ten")])
def test_minutes(test_minutes, expected):
    assert convert_minutes_to_text(test_minutes) == expected


@pytest.mark.parametrize("test_hours,expected", [(5,"five"), (10, "ten")])
def test_minutes(test_hours, expected):
    assert convert_hours_to_text(test_hours) == expected

@pytest.mark.parametrize("test_times, expected", [("1:00", "One o'clock"), ("2:00", "Two o'clock"), ("13:00", "One o'clock"),  ("13:05", "Five past one"), ("13:10", "Ten past one"), ("13:25", "Twenty five past one"), ("13:30", "Half past one"), ("13:35", "Twenty five to two"), ("13:55", "Five to two"), ("01:45", "Quarter to two")])
def test_TalkingClock_get_time(test_times, expected):
    assert TalkingClock(["filename", test_times]) ==  expected

@pytest.mark.parametrize("test_random", [("20:100"), ("-1:10"), ("10::10"), ("10"), (-10), (10), ("20:a")])
def test_random_input(test_random):
    assert TalkingClock(["filename", test_random]) == "\nusage: TalkingClock.py [HH:MM]\n"




