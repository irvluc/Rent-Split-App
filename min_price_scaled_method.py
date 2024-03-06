###########################################################################
### Method 2 - Scale the rent based upon minimum price and bedroom size ###
###########################################################################

# This method takes a minimum price per room, e.g. lowest price anyone is willing to pay or the cheapest room price that is available in a similar area, subtracts that from the total rent price, and then distributes the remaining rent based upon total floor size of every room excluding the smallest. The smallest room will be priced at the minimum price specified earlier, and the remaining rooms are priced prpportionally above the minimum depending on their size. 

### Example: 5 bed house with varying room sizes ###

## 1. Inputs ##
# Bedroom 1 
room_1_width = 4.48
room_1_length = 3.72

# Bedroom 2 
room_2_width = 3.81
room_2_length = 3.22

# Bedroom 3
room_3_width = 5.23
room_3_length = 4.61

# Bedroom 4
room_4_width = 3.80
room_4_length = 3.22

# Room 5
room_5_width = 3.49
room_5_length = 3.33

# Total Rent 
total_rent_pcm = 4250

# Minimum price for a room (either user decides or an average of cheapest room on the market - .e.g figure here is for cheapest bedroom to rent in Hackney, London)
min_rent = 650


## 2. Calculations ##
# Area per bedroom (sqm)
room_1_area = room_1_width * room_1_length
room_2_area = room_2_width * room_2_length
room_3_area = room_3_width * room_3_length
room_4_area = room_4_width * room_4_length
room_5_area = room_5_width * room_5_length

# Total bedroom area (sqm) excluding smallest room

room_area_sizes = [room_1_area, room_2_area, room_3_area, room_4_area, room_5_area]

total_room_area = sum(room_area_sizes)

sorted_sizes = sorted(room_area_sizes)

sorted_sizes.remove(min(room_area_sizes)) 

total_area_excl = sum(sorted_sizes)


# Rent left to be distributed after charging minimum price per room
remaining_rent = total_rent_pcm - (5 * min_rent)

remaining_rent_per_sqm = remaining_rent / total_area_excl

# Rent prices per room

room_1_rent = min_rent + (room_1_area * remaining_rent_per_sqm)

room_2_rent = min_rent + (room_2_area * remaining_rent_per_sqm)

room_3_rent = min_rent + (room_3_area * remaining_rent_per_sqm)

room_4_rent = min_rent + (room_4_area * remaining_rent_per_sqm)

room_5_rent = min_rent

# Proportion of rents per room (%)

room_1_proportion = room_1_rent / total_rent_pcm
room_2_proportion = room_2_rent / total_rent_pcm
room_3_proportion = room_3_rent / total_rent_pcm
room_4_proportion = room_4_rent / total_rent_pcm
room_5_proportion = room_5_rent / total_rent_pcm


### 3. Outputs ### 

print(f"The rent should be split as follows: \n Room 1 pays £{round(room_1_rent, 0)} ({round(room_1_proportion * 100, 0)}%) \n Room 2 pays £{round(room_2_rent, 0)} ({round(room_2_proportion * 100, 0)}%) \n Room 3 pays £{round(room_3_rent, 0)} ({round(room_3_proportion * 100, 0)}%) \n Room 4 pays £{round(room_4_rent, 0)} ({round(room_4_proportion * 100, 0)}%) \n Room 5 pays £{round(room_5_rent, 0)} ({round(room_5_proportion * 100, 0)}%)")