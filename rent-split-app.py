import streamlit as st
import numpy as np
import pandas as pd

# Add title and instructions

st.title("Rent Splitting App")
st.caption("Enter room size information and submit for a fair split of rent between your housemates")

st.subheader("1. Enter Total Number of Bedrooms 🛏️")

no_of_bedrooms = st.number_input(      
        label = "No. of Bedrooms",
        value = 3,
        step = 1, 
        max_value = 10,
        min_value = 2
    )

st.subheader("2. Enter Total Monthly Rent Amount💲")

total_rent_pcm = st.number_input(      
        label = "Rent (£)",
        value = 3000,
        step = 1, 
    )


st.subheader("3. Enter Minimum Rent Amount for a Room 🐭")

min_rent = st.number_input(      
        label = "Minimum per Room (£)",
        value = 50,
        step = 1, 
        min_value = 1,
        max_value = int(total_rent_pcm / no_of_bedrooms)
    )


st.subheader("4. Enter Room Size Dimensions 📏")

col_1, col_2 = st.columns(2)

width_dynamic_labels = []
width_dynamic_values = []

length_dynamic_labels = []
length_dynamic_values = []

with col_1:
    for i in range(no_of_bedrooms):
        width_dynamic_labels.append(f"Room {i + 1} Width (m)")
        width_dynamic_values.append(st.number_input(      
            label = width_dynamic_labels[i],
            value = 3.45,
            step = 0.01
        ))

with col_2:
    for i in range(no_of_bedrooms):
        length_dynamic_labels.append(f"Room {i + 1} Length (m)")
        length_dynamic_values.append(st.number_input(      
            label = length_dynamic_labels[i],
            value = 3.45,
            step = 0.01
        ))    



if st.button(label="Click for Rent Split", use_container_width=True): 
    ## 2. Calculations ##

    room_area_sizes = []
    # Area per bedroom (sqm)
    for i in range(no_of_bedrooms): 
        room_area_sizes.append(width_dynamic_values[i] * length_dynamic_values[i])


    total_room_area = sum(room_area_sizes)

    sorted_sizes = sorted(room_area_sizes)

    sorted_sizes.remove(min(room_area_sizes)) 

    total_area_excl = sum(sorted_sizes)


    # Rent left to be distributed after charging minimum price per room
    remaining_rent = total_rent_pcm - (no_of_bedrooms * min_rent)

    remaining_rent_per_sqm = remaining_rent / total_area_excl





    room_rents = []
    room_proportions = [] 

    for i in range(no_of_bedrooms):
        room_rents.append(min_rent + (room_area_sizes[i] * remaining_rent_per_sqm))    

    room_rents[room_rents.index(min(room_rents))] = min_rent

    for i in range(no_of_bedrooms):
        room_proportions.append(room_rents[i] / total_rent_pcm)    
        

    for i in range(no_of_bedrooms):
        st.subheader(f"Room {i + 1} should pay: £{round(room_rents[i], 0)} ({round(room_proportions[i] * 100, 0)}%)")


  

