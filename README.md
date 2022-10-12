
![Status](https://github.com/maxsimmonds1337/Talking-Clock/actions/workflows/python-app.yml/badge.svg?event=push)

# Talking-Clock
Talking clock code for Lloyds Banking group. This is a python application that either takes a time input as a string, "10:10", and returns the time in words, "Ten past ten". Or, if no time input string is given, it returns the current time (in GMT).

The application works as a standalone application run from the CLI, using the command (from the root directory of this repo):

```
./TalkingClockFlask/TalkingClock/TalkingClock.py time
```
Where time is an optional string input, such as "10:10".

The application also works as a REST service. It uses the Flask frame work, and can be run locally with the command:

```
./TalkingClockFlask/bootstrap.sh
```

This runs a shell script that invokes flask and calls the python script. It can then be accessed locally here <a>localhost:5000/</a>

One can either use this as an API, and POST data to the URL, or visit the site. The root directory of the website is the endpoint for the current time. To request a time, simply append it to the end <a>localhost:5000/10:10</a>

Finally, the python application is also hosted on a heroku server, here - <a>https://talking-clock.herokuapp.com/</a>. Again, one can visit this site the same as in the above example with the locally hosted application, or, one can utilise the REST API and POST a request with the payload {"time": ""}. This will return the current time. To request a specific time the payload should be {"time": "10:10"}, where 10:10 is the specific time.

An example of this can be seen here - <a href = "https://maxsimmonds.engineer/programming/python/TalkingClock/TalkingClock.html"> https://maxsimmonds.engineer/programming/python/TalkingClock/TalkingClock.html </a>

The above uses javascript to call the API hosted on heroku. Due to the cross origin request, it uses a CORS proxy hosted on cloudflare - <a href = "https://cors-proxy.maxsimmonds1337.workers.dev"> https://cors-proxy.maxsimmonds1337.workers.dev </a>. This I wrote to take POST requests and forward them on based on GET parameter sent in the URL. Only the maxsimmond.engineer domain is whitelisted though, so other websites cannot make CORS proxy requests.

## Installation

To run this locally, install the following dependancies:

```
pip install Flask, pipenv, pytest, gunicorn==20.0.4
```

or, install from the requirements.txt:

```
 pip install -r requirements.txt
 ```

Remember to update your PATH variables if needed! The ``` --user ``` may be required for install.

## Usasge

### Running Tests

Tests are run as a github action when code is pushed to main, but to run tests locally, run "pytest" in ./TalkingClockFlask/TalkingClock/ :
```
pytest
```

### REST API
Run the bootstrap executable, and navigate to <a>localhost:5000/</a>

```
./bootstrap.sh
```

If you would like to request a time, then navigate to <a>localhost:5000/10:10</a>

## Objectives 

Within the team, we don't like clocks that display as numbers. In fact, we like clocks that present the current time in a more "Human Friendly" way.

Objective 1

Write a command-line program that returns the current time using the "Human Friendly Text" demonstrated in the example below.

 

Numeric Time Human Friendly Text

 

- 1:00 One o'clock
- 2:00 Two o'clock
- 13:00 One o'clock
- 13:05 Five past one
- 13:10 Ten past one
- 13:25 Twenty five past one
- 13:30 Half past one
- 13:35 Twenty five to two
- 13:55 Five to two
 

For example, if we execute this program at 16:30, it should output "Half past four"

 

$ ..some command..
Half past four

Objective 2

Allow the command to take an arbitrary Numeric Time parameter as input and return the "Human Friendly Text" equivalent.

For example:

$ ..some command.. 15:00
Three o'clock
$

Objective 3

Write a REST service to expose the clock and allow an optional parameter to pass the arbitrary Numeric Time like Objective 2, returning the "Human Friendly Text" as JSON.

Additional Info & Tips

- Please supply Clean and Readable, Production Ready Code and Scripts
- You can use Any Language, Any Library or Any Framework to complete the objectives
- Additional points awarded for supplying Valid and Passing Unit Tests
