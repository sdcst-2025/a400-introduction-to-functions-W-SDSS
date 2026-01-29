"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
import random

def title():
  print("---Number Guessing Game!!---")
  print("I am thinking of a number 1 to 10.")
  print("Try to guess it")

def game():
  num = random.randint(1, 11)
  guess = 0
  while guess != num:
    guess = int(input("Enter your guess: "))
    if guess < num:
      print("Its too low")
    elif guess > num:
      print("its too high")
    else:
      print("correct!")
      
