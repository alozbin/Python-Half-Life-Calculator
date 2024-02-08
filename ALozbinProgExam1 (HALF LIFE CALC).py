#Anthony Lozbin
#U08906243
#This program calculates either the half-life of a substance, or the amount of a substance remaining after a given time. Any other
#input produces the output 'Sorry, invalid choice.'

import math

print('This program can calculate the half-life of an isotope, T (in years) or the amount of an isotope remaining, N (in grams).')
user_input = input('Please indicate which calculation to make (enter \'N\' or \'T\'): ')

if user_input == 'N':
    N_t = user_input
    N_0 = float(input('Enter the initial amount of the substance (in grams): '))
    T = float(input('Enter the half-life of the substance (in years): '))
    t = float(input('Enter the time measured since substance decay (in years): '))
    N_t = N_0 * (math.e ** ((-0.693 * t) / T))
    print(f'The amount of substance remaining after {t} years is {N_t:.3f} grams')
elif user_input == 'T':
    T = user_input
    N_0 = float(input('Enter the original quantity of the substance (in grams): '))
    N_t = float(input('Enter the amount of the substance remaining (in grams): '))
    t = float(input('Enter the time measured since substance decay (in years): '))
    ln_n = N_t / N_0
    T = (-0.693 * t) / (math.log(ln_n, (math.e)))
    print(f'The half-life of the substance after decaying from {N_0} grams to {N_t} grams is {T:.3f} years.')
else:
    print('Sorry, invalid choice.')
