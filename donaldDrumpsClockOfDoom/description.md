# Dondald Drump's Clock of Doom

Donald Drump is a mad scientist. As with all mad scientists he has built his
own doomsday clock, once the clock runs out of time a giant nuclear explosion
will destroy the earth in a giant fiery explosion. Sad. 

Because he thought that the danger of prolonged exposure to radioactive plutonium was
"fake news" Drump died recently. You have been sent in to disable the doom
clock using a 4 digit pass code hidden in his notes. 

His notes have 4 sets of 4 times (24 hr military times), you have determined 
that each set of times corresponds to one of the 4 digits of the disable code.
Reading further in his notes you see that the method he used was as follows:

1. Add all the hours and minutes together separately
2. Make sure all numbers are within the correct range accepted for related time values (hours: 0-23, minutes: 0-59)
3. Sum the hours and minutes results together and make sure it is within the range of 0-42
4. sum individual digits together until a single digit number is reached

Notes:
- You have determined through trial and error that if a number is out of its given range, Drump loops back to the beginning and continues the counting.