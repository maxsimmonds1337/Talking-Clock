# content of test_sample.py
from TalkingClock import *
import pytest
from time import localtime, strftime 

@pytest.mark.parametrize("test_minutes,expected", [(1,"one"), (2,"two"), (3,"three"), (4, "four"), (5,"five"), (6,"six"), (7,"seven"), (8,"eight"), (9, "nine"), (10, "ten"), (11, "eleven"), (12, "twelve"), (13, "thirteen"), (14, "fourteen"), (15, "fithteen"), (16, "sixteen"), (17, "seventeen"), (18, "eighteen"), (19,"nineteen")])
def test_minutes(test_minutes, expected):
    assert convert_minutes_to_text(test_minutes) == expected


@pytest.mark.parametrize("test_hours,expected", [(1,"one"), (2,"two"), (3,"three"), (4, "four"), (5,"five"), (6,"six"), (7,"seven"), (8,"eight"), (9, "nine"), (10, "ten"), (11, "eleven"), (12, "twelve"), (13, "one"), (14, "two"), (15, "three"), (16, "four"), (17, "five"), (18, "six"), (19,"seven"), (20,"eight"), (21,"nine"), (22,"ten"), (23,"eleven"), (00,"twelve")])
def test_minutes(test_hours, expected):
    assert convert_hours_to_text(test_hours) == expected

@pytest.mark.parametrize("test_times, expected", [("1:00", "One o'clock"), ("2:00", "Two o'clock"), ("13:00", "One o'clock"),  ("13:05", "Five past one"), ("13:10", "Ten past one"), ("13:25", "Twenty five past one"), ("13:30", "Half past one"), ("13:35", "Twenty five to two"), ("13:55", "Five to two"), ("01:45", "Quarter to two"), ("00:00", "Twelve o'clock"),("00:01", "One past twelve")])
def test_TalkingClock_get_time(test_times, expected):
    assert TalkingClock(["filename", test_times]) ==  expected

def test_no_inputs():
    print(TalkingClock("filename"))

@pytest.mark.parametrize("test_random", [("20:100"), ("-1:10"), ("10::10"), ("10"), (-10), (10), ("20:a"), ("a"), ("a:a")])
def test_random_input(test_random):
    assert TalkingClock(["filename", test_random]) == "\nusage: TalkingClock.py [HH:MM]\n"

def test_extra_inputs():
    print(TalkingClock(["filename", "arg1", "arg2"]))


