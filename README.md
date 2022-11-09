# guessComputer.py
This file was a project assigned for my CIS 214 class at Georgia Military College, Summer Semester 2021

## Description
User enters a range of numbers and selects a number within that range. The
computer then guesses the user's number using the built-in randint() method.

1. The program requests three inputs  
&nbsp;&nbsp;&nbsp;a. The smallest number in the range  
&nbsp;&nbsp;&nbsp;b. The largest number in the range  
&nbsp;&nbsp;&nbsp;c. The user's number  
   The program rejects inputs that are not integers for all requests; when this
   happens, the program requests input again.

2. The count to count the computer's number of guesses is initialized to 0

3. The computations and outputs are  
&nbsp;&nbsp;&nbsp;a. For each iteration  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i. Compute a random number within the user's range  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii. Determine whether the number is larger or smaller than the user's number  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii. If the computer-generated number is either larger or smaller  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. print the computer-generated number along with a message saying whether the number is too small or too large  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iv. if the computer-generated number matches the user's number  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. print the computer-generated number along with count, the number of tries  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. terminate loop
