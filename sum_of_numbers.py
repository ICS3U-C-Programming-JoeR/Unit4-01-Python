#!/usr/bin/env python3
# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Joe rugezo
# Modified on: Nov 13, 2023
# This program asks the user to enter a positive number and then uses a loop to calculate and display the sum  of all numbers from 0 until that number.

def main():
  loop_counter = 0
  sum = 0

  user_number = int(input("Enter a positive number: "))
  print("")

  while (loop_counter <= user_number):
    sum = sum + loop_counter
    print("Tracking {0} times through loop.".format(loop_counter))
    loop_counter = loop_counter + 1
  
  print("")
  print ("The sum of the numbers from 0 to {} is: {}.".format(user_number, sum))

if __name__ == "__main__":
  main()