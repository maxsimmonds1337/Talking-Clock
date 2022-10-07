# Talking-Clock
Talking clock code for Lloyds Banking group

Within the team, we don't like clocks that display as numbers. In fact, we like clocks that present the current time in a more "Human Friendly" way.

Objective 1

Write a command-line program that returns the current time using the "Human Friendly Text" demonstrated in the example below.

 

Numeric Time Human Friendly Text

 

1:00 One o'clock
2:00 Two o'clock
13:00 One o'clock
13:05 Five past one
13:10 Ten past one
13:25 Twenty five past one
13:30 Half past one
13:35 Twenty five to two
13:55 Five to two
 

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