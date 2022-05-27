import streamlit as s
import pandas as pd

s.title('My Parents New Healthy Diner')

s.header('Breakfast FAvourites')
s.text('🥣 Omega 3 & Blueberry Oatmeal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-Boiled Free-Range')
s.text('🥑🍞 Avocado Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = pd.read_csv("fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_selected = s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#s.dataframe(my_fruit_list)
s.dataframe(fruits_to_show)

#New Section to import FruityVice API response
s.header('Fruityvice Fruit Advice!')
import requests as r
fruityvice_response = r.get("https://Fruityvice.com/api/fruit/" + "Kiwi")
#s.text(fruityvice_response.json()) 

fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
s.dataframe(fruityvice_normalized)
