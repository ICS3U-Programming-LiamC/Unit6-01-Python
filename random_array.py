#!/usr/bin/env python3

# Created by: Liam Csiffary
# Created on: June 6, 2021
# This program generates 10 random numbers then
# it calculates the average of them

# import the necessary modules
import random
import const


# greet the user
def greet():
    print("Welcome! This program generates 10 random numbers and will then\
find the average of all these numbers")


# main function
def main():
    # initialize the list
    array_of_nums = []
    # generate 10 random numbers and add them to the list
    for each in range(0, const.NUM_NUMS):
        array_of_nums.append(random.randint(const.MIN, const.MAX))

    # set total to zero and then add each element in the list
    # to the total
    total = 0
    for each in array_of_nums:
        total = total + each

    # find the average by dividing the total by the number of numbers
    average = total / len(array_of_nums)

    # print all these things back to the user
    print(array_of_nums)
    print("All the numbers added up = {}".format(total))
    print("The average of all these numbers is {}".format(average))


# gets the program started
if __name__ == "__main__":
    greet()
    main()
