#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Jan 2022
# This program generates a 2D list

import random


def average_of_numbers(passed_in_2D_list, rows, columns):
    # this function calculates the average of the 2D list

    average = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            average += single_element

    average = average / (rows * columns)

    return average


def main():
    # this function uses a 2D list

    a_2d_list = []

    # input
    rows = input("How many row would you like: ")
    columns = input("How many columns would you like: ")
    print("\n")

    try:
        int_rows = int(rows)
        int_columns = int(columns)

        if int_rows > 0 and int_columns > 0:
            for loop_counter_rows in range(0, int_rows):
                temp_column = []
                for loop_counter_columns in range(0, int_columns):
                    a_random_number = random.randint(1, 50)
                    temp_column.append(a_random_number)
                    print("{0} ".format(a_random_number), end="")
                a_2d_list.append(temp_column)
                print("")
            print(" ")

            # call function
            average = average_of_numbers(a_2d_list, int_rows, int_columns)
            print("The average of all the numbers is: {0} ".format(average))

        else:
            print("Please enter a positive number.")

    except Exception:
        print("This is not a number")

    print("\nDone.")


if __name__ == "__main__":
    main()
