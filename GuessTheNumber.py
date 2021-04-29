#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 00:10:50 2021

@author: Alex Testa
"""
import Function as fn

number = fn.create_number_from_range(0,100)

fn.tips(number)
fn.decrease_life()

for counter in range(5):
    result = fn.game_logic(number, fn.take_correct_number())
    if  result == -1:
        print ('You have lost')
        break

