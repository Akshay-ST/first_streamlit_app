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

s.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado', 'Strawberries'])

s.dataframe(my_fruit_list)

