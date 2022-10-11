#!/bin/sh
export FLASK_APP=./TalkingClock/TalkingClock.py

pipenv run flask --debug run -h 0.0.0.0