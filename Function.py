#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:14:47 2021

@author: Alex Testa
"""

import random as rnd
import numpy as np

life = 5

def create_number_from_range(start, stop):
    return rnd.randint(start, stop)

def tips(number):
    if number % 2 == 0:
        print('The number is even')
    elif number % 3 == 0:
        print('The number is odd')
    else:
        print('The number is prime')

def take_correct_number():
    while True:
        try: 
            number = int(input('Give me a number > 0 and < 100 : '))
            if number > 100 or np.sign(number) == -1: 
                print('Plase, take me a correctly number ( < 0 and > 100)')
            else:
                return number
        except:
            print('Take me a number ;)')

def decrease_life():
    global life
    life -= 1
    print('Attemps : ', life)


def game_logic(number_to_guess, take_correct_number):
        decrease_life()
        if life == 0:
            return -1
        elif number_to_guess < take_correct_number: 
             print('Your number is bigger than the guess number')
        elif number_to_guess > take_correct_number:
             print('Your number is lower than the guess number')

        