# Name Tanner Huck
# CSE 160
# Midterm_au22

# Problem 1.
# Writing a function that will take in a list of strings in the
# form mm/dd/yy and will return the average of the days


def find_days(dates_list):
    sum_days = 0  # Total value of dates
    count_days = 0  # Total number of dates in list
    for dates in dates_list:  # Loop to run through each date
        count_days = count_days + 1  # Updating number of dates
        specific_date = dates[3] + dates[4]  # Collecting the date
        num_specific_date = int(specific_date)  # Turning date into int
        sum_days = sum_days + num_specific_date  # Adding int into sum
    avg_days = sum_days // count_days  # Calculating avg of dates
    return avg_days  # Returns the avg


# Testing the Function
assert find_days(["12/12/12", "02/02/12", "05/10/13"]) == 8
assert find_days(["03/08/92", "11/01/19"]) == 4
assert find_days(["06/16/13", "06/16/13"]) == 16


# Problem 2.
# Writing a function that will take a list of weathers and temps
# it will find the highest temp when the weather is clear and return
# the index when these conditions are met and the temp


def plan_trip(weather, temps):
    if weather == [] or temps == []:  # If we are given empty list
        return "Missing Data!"  # Return string saying we are missing data
    else:  # If we don't have an empty list
        # Create variables for the highest temp, the index of the temp,
        # and number of clear days
        current_high_temp = 0
        index_of_high = 0
        num_of_clear = 0
        for forcast in temps:  # Loop through each temp
            date = temps.index(forcast)  # Index of given temp
            # If it is a clear day and we have a new highest temp
            if str(weather[date]) == "clear" and forcast > current_high_temp:
                # Update variables with new highest temp
                current_high_temp = forcast
                index_of_high = date
                num_of_clear = 1
        if num_of_clear > 0:  # If we saw at leat one clear day
            # Return index and high temp
            return [index_of_high + 1, current_high_temp]
        else:  # If no clear days
            return ("No Clear Weather!")  # Return staying no clear days


# Testing the Function
assert plan_trip(["sunny", "rainy", "clear", "clear"],
                 [39, 37, 22, 30]) == [4, 30]
assert plan_trip(["clear", "sunny", "rainy"], []) == "Missing Data!"
assert plan_trip(["sunny", "rainy", "rainy", "sunny"],
                 [39, 37, 22, 30]) == "No Clear Weather!"


# Problem 3.
# Writing a function that will take in a list of resturants and their
# ratings, as well as a base rating. The function will return a list
# of all the resturants with a rating greater than the base raiting
# and sorted by name


def recommend_restaurant(restaurants, min_rating):
    good_food = []  # list of good resturants
    # Loop through each restaurnant and review
    for location in restaurants:
        if location[1] >= min_rating:  # If it is a good rating
            good_food.append(location[0])  # add to recomend list
    good_food = sorted(good_food)  # sort list
    return good_food


# Testing the function
assert recommend_restaurant([["shawarma king", 4.4], ["cedars", 4.2],
                            ["chipotle", 3.6],
                            ["nuodle express", 2.9]], 3.6) == \
                                ["cedars", "chipotle", "shawarma king"]
assert recommend_restaurant([], 5) == []
assert recommend_restaurant([["cedars", 4.2],
                            ["shawarma king", 4.4], ["chipotle", 3.6],
                            ["nuodle express", 2.9]], 5) == \
                                []


# Problem 4.
# Writting a fucntion that will take a list and make a new list
# by adding on more elements. The second input will determine how
# many elements will be in the final list. The third input will
# determine how to come up with the new added elements, an input
# of n means it will take a sum of the last n elements in the list
# and the sum becomes the new element.


def zombie_list(initial_list, output_list, bunch_size):
    # Creating list we will later return
    final_list = initial_list[:]
    # Calculating how many element we will add to the initial list
    diff_length = output_list - len(initial_list)
    # Loop that will run howevery many times we want to add
    # a new element
    for i in range(0, diff_length):
        new_element = 0  # The new element we will add to the list
        # Loop that will run through the last "bunch_size" elements
        # and add them to the new element
        for j in range(0, bunch_size):
            new_element = new_element + final_list[-1 - j]
        # Adding the new element to the final list
        final_list.append(new_element)
    return(final_list)  # Returning the final list


# Testing the function
assert zombie_list([1, 2, 3], 6, 2) == [1, 2, 3, 5, 8, 13]
assert zombie_list([4, 1, -2, 3], 9, 3) == \
                    [4, 1, -2, 3, 2, 3, 8, 13, 24]
assert zombie_list([0, -4, -2], 10, 1) == \
                    [0, -4, -2, -2, -2, -2, -2, -2, -2, -2]


# Problem 5.


def plot_flowers(placements, num_rows, num_cols):
    # Creating a final list that will later be returned
    flower_grid = []
    # Loop that will run for howevery many rows there are
    for row in range(num_rows):
        new_row = []  # Creating a temperary row
        # for loop that will run through how every many cols there are
        for col in range(num_cols):
            new_row.append(0)  # Adding a 0 to the temp row
        flower_grid.append(new_row)
    # for loop that will run through the placements and replace the 0
    # wih 1 whenever the folwer will go
    for index in placements:
        flower_grid[index[0]][index[1]] = 1
    return flower_grid


# Testing the function
assert plot_flowers([[1, 2], [0, 3], [2, 1], [0, 2]], 3, 4) == \
                    [[0, 0, 1, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
assert plot_flowers([], 3, 2) == [[0, 0], [0, 0], [0, 0]]
assert plot_flowers([[0, 0]], 1, 1) == [[1]]


###
# Collaboration: Jaiden Atterbury - jatter41
