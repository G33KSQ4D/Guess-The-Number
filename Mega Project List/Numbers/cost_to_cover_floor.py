# Created April 1st, 2018 (Happy April Fools - No easter eggs here sorry, maybe next time)

# Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width
# and height, using a cost entered by the user.

import math # To use math.ceil()

# I replace height with length because I mean, I think the person who created these challenges
# Made a mistake. Area is l * w not w * h (That would be area of the base or something)

# I may have misunderstood this question, not certain
floor_width = float(input("Enter width of floor:\t\t"))
floor_length = float(input("Enter length of floor:\t\t\n"))
floor_area = floor_width * floor_length

tile_width = float(input("Enter width of a tile:\t\t"))
tile_length = float(input("Enter length of a tile:\t\t\n"))
tile_area = tile_width * tile_length
tile_cost = float(input("Enter cost of 1 tile:\t\t\n"))

# I do floor_area / tile_area to get number of tiles needed
# I did math.ceil(..) because there might be a remainder of floor left
# So just buy an extra tile incase
number_of_tiles = math.ceil(floor_area / tile_area)
total_cost = tile_cost * number_of_tiles

print("You will need ${0} to buy {1} tiles.\n".format(total_cost, number_of_tiles))