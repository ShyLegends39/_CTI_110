# A brief description of the project: This code is for calculating and processes and displays your travel expense(s).
# Also, the words: destination, accommodation, are abbreaviated in those variables to save time and avoid mistakes, also that they wouldn't be too long?!?
# This is add on this program from P1HW2! In other word, this program gets updates with what is asked for in this assignment & correcting mistakes from last time in P1HW2.

# 10/4/2022

# CTI-110 P2HW1 - Travel 

# Kelly Bullard

#


# Some info on this program 's code
print('This program calculates and displays travel expences')
print('') # The space in-between the lines

# Inputs for the Travel Expences with output prompts

# User's input for the amount for their budget
print('Enter Budget: ', end='')
amountBudget = int(input())
print('') # The space in-between the lines

# User's input for the travel destination
print('Enter your travel destination: ', end='') 
travelDestn = input()
print('') # The space in-between the lines

# User's input for the expences' amount of the gas
print('How much do you think you will spend on gas? ', end='')
amountGas = int(input())
print('') # The space in-between the lines

# User's input for the expences' amount for the accomodation
print('Approximately, how much will you need for accomodation/hotel? ', end='')
amountAccomm = int(input())
print('') # The space in-between the lines

# User's input for the expences' amount for food
print('Last, how much do you need for food? ', end='')
amountFood = int(input())
print('') # The space in-between the lines

# Outputs for the Travel Expences

# The outputs and results of the user's inputs
print('------------Travel Expences------------')
print('Location:          ',travelDestn)
print(f'Initial Budget:     ${amountBudget:.1f}')
print(f'Fuel:               ${amountGas:.1f}')
print(f'Accomodation:       ${amountAccomm:.1f}')
print(f'Food:               ${amountFood:.1f}')
print('---------------------------------------')
print('') # The space in-between the lines

# The calculations of the results of the user's inputs
totalExpences = amountGas + amountAccomm + amountFood
finalBalance = amountBudget - totalExpences
# The over-all expences' amount for the budget for the travel expences
print(f'Remaining Balance:  ${finalBalance:.1f}')


# Pseudocode for this program's code
# NOTE: For this use the current Python(like Python 3) by using the following inputs and outputs and more for program's code.
# Also, I am translating the updates from P2HW1 into this pseudocode code and will trim this pseudocode code.

# START

# Some info on this code
# DISPLAY 'This program calculates and displays travel expences'
# DISPLAY '' # The space in-between the lines

# Inputs for the Travel Expences with output prompts

# User's input for the amount for their budget
# DISPLAY 'Enter Budget: ', ADD: end='', the user's input is on the prompt line
# INPUT amountBudget = Integer(input())
# DISPLAY '' # The space in-between the lines

# User's input for the travel destination
# DISPLAY 'Enter your travel destination: ', ADD: end='', the user's input is on the prompt line
# INPUT travelDestn = input()
# DISPLAY '' # The space in-between the lines

# User's input for the expences' amount of the gas
# DISPLAY 'How much do you think you will spend on gas? ', ADD: end='', the user's input is on the prompt line
# INPUT amountGas = Integer(input())
# DISPLAY '' # The space in-between the lines

# User's input for the expences' amount for the accomodation
# DISPLAY 'Approximately, how much will you need for accomodation/hotel? ', ADD: end='', the user's input is on the prompt line
# INPUT amountAccomm = Integer(input())
# DISPLAY '' # The space in-between the lines

# User's input for the expences' amount for food
# DISPLAY 'Last, how much do you need for food? ', ADD: end='', the user's input is on the prompt line
# INPUT amountFood = Integer(input())
# DISPLAY '' # The space in-between the lines

# Outputs for the Travel Expences

# NOTE: The spacing won't match the real code because of the word 'Float' on those lines with it.
# Also, on the part with like for EX: ${amountBudget:.1f}' is left as is, because not sure how to make into pseudocode code? I hope that is okay?

# The outputs and results of the user's inputs
# DISPLAY '------------Travel Expences------------'
# DISPLAY 'Location:          ',travelDestn
# DISPLAY Float'Initial Budget:     ${amountBudget:.1f}'
# DISPLAY Float'Fuel:               ${amountGas:.1f}'
# DISPLAY Float'Accomodation:       ${amountAccomm:.1f}'
# DISPLAY Float'Food:               ${amountFood:.1f}'
# DISPLAY '--------------------------------------'
# DISPLAY '' # The space in-between the lines

# The calculations of the results of the user's inputs
# CALCULATE totalExpences = amountGas + amountAccomm + amountFood
# CALCULATE finalBalance = amountBudget - totalExpences
# The over-all expences' amount for the budget for the travel expences
# DISPLAY Float'Remaining Balance:   ${finalBalance:.1f}'

# END

#
